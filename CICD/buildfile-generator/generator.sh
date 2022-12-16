echo $1
if  [ $1 == 'rollback' ] #渲染回退流水线
then
  cp helmignore.rollback  .helmignore
  target="../../helmfile/.coding.rollback.yaml"; echo $target; helm template coding-buildfile-generator ./  |grep ^version -A 10000 > $target;
elif [ $1 == 'build' ]; then #渲染所有服务流水线
  cp helmignore.build  .helmignore
  for i in `ls config/|grep ^bus-`;do echo $i; target="./helmfile/${i: 4}/.coding.build.yaml"; echo $target; helm template coding-buildfile-generator ./ -s templates/configmap.yaml -f config/$i/values.yaml |grep ^version -A 10000 > $target; done
  # generate main pipeline coding build yaml: templates/main-pipeline.coding.configmap.yaml  -> templates/main-pipeline.coding.build.yaml 
  main_pipe_target="./main-pipeline.coding.build.yaml" 
  helm template main-pipeline-template ./ -s templates/main-pipeline.coding.configmap.yaml |grep ^version -A 10000 > $main_pipe_target
fi


