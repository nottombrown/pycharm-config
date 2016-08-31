brew install awscli

export AWS_ACCESS_KEY_ID="AKIAJ7V4FOJ3FRK7QFTA"
export AWS_SECRET_ACCESS_KEY="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"

export env_id='VNCSeaquestSlow-v0'
aws s3 cp --recursive s3://openai-vnc-demonstrations/$env_id/ /tmp/$env_id/

#for demonstrator_id in /tmp/$env_id/demonstrator_*; do
#  for file in $demonstrator_id/*.tar.gz; do
#    tar -zxvf $file $(echo $file | sed s/.tar.gz//);
#  done;
#done
