%KGCB Run
%{
%%
%THIS PART GENERATES THE TRUTH FOR A GAUSSIAN PROCESS
%SPITS OUT 
%x (THE ALTERNATIVES)
%mu_0 (PRIOR BELIEF ABOUT MEAN)
%mu (THE MEAN (TRUTH))
%covM (THE COVARIANCE MATRIX)

%Let's generate a so called Gaussian Process with zero mean on [1,100]

x=(1:100)'; %domain of the problem

mu_0=0*ones(100,1); %our prior beliefs about the mean
%equivalent to mu_0=zeros(100,1)

%this is the main parameter (rho is between 0 and 1)
%you can play around with the values to see what happens as rho changes
rho=0.10;

%generate the covariance matrix
    M=length(x);
    covM=zeros(M,M);

    %the matrix will be symmetric
    %instead of looping over all elements, just loop over the first half
    for i=1:M
        for j=(i+1):M
            covM(i,j)=0.5*exp(-(abs(i-j)/((M-1)*rho))^2);
        end
    end

    %and copy the rest to the other part
    covM=covM+covM';
    covM=covM+diag(0.5*ones(M,1));

    
%generate the truth using the covariance matrix and the mean
mu=mvnrnd(mu_0,covM);

%To see what the functions looks like in the domain [1,100]
plot(x,mu);

%%
%THIS PART RUNS THE KGCB ON THE VALUES GENERATED BY ABOVE

%Set the measurement variance (lambda)
lambda=0.25;
beta_W=1/lambda*ones(M,1);
%Precision(Beta)=1/Variance
%}
%Run the KGCB N many times
N=40;
mu = [61.65;52.69;66.87;68.12;52.68;57.79;78.98;62.24;84.98;77.22;94.64;66.38;73.14;71.83;56.8;62.82;82.68;40.75;92.46;105.34;75.61;71.97;89.28;55.64;68.23;59.27;53.83;55.08;64.86;69.97;85.51;93.99;96.32;71.54;63.69;77.77;98.5;102.79;108.17;76.76;90.97;92.17;75.53;68.79;76.54;77.76;89.42;81.84;77.83;61.09;81.54;73.78;108.64;80.38;38.64;47.12;86.35;61.57;45.94;60.02;63.42;84.59;69.86;67.57;38.59;62.15;56.01;50.08;54.3;92.42;44.82;51.31;49.55;48.24;59.1;65.12;88.02;46.09;50.39;54.68;85.11;53.7;65.35;66.55;53.62;74.79;39.65;37.36;22.16;45.72;42.02;34.27;59.93;77.4;37.57;23.65;42.22;55.1;59.55;55.91;61.37;27.73;60.13;53.39;77.41;78.63;98.06;90.48;62.85;56.92;23.66;61.78;38.8;45.29;56.11;48.36;56.95;74.42;42.88;28.96;92.29;83.33;97.51;98.76;83.32;88.43;82.32;65.58;88.32;80.56;97.98;69.72;74.45;73.14;58.11;64.13;83.99;42.06;84.19;97.07;67.34;63.7;81.01;47.37;60.61;51.65;44.18;45.43;45.63;50.74;45.24;44.14;58.16;53.0;41.39;52.95;71.95;64.63;58.32;58.22;70.7;55.66;55.26;46.49;36.27;52.94;62.87;45.33;94.19;77.45;68.57;60.81;86.09;57.83;56.29;55.19;75.49;70.33;50.94;62.5;91.47;73.73;77.93;76.33;72.92;83.56;90.34;55.08;71.95;94.9;72.87;72.72;79.63;78.32;61.88;67.9;79.19;37.26;72.1;64.78;64.59;64.49;74.41;59.37;72.01;54.27;49.75;48.15;58.52;69.16;78.38;43.33;81.64;70.22;55.96;47.09;88.16;101.04;78.19;74.55;77.98;44.34;91.42;82.65;76.05;92.72;110.42;92.88;90.82;55.56;52.92;75.87;78.46;78.31;95.77;60.72;88.24;76.82;70.85;61.98;86.13;77.17;71.73;72.98;82.76;87.87;82.69;91.17;93.5;68.72;60.87;74.95;74.03;78.32;83.7;52.29;66.5;67.7;66.7;59.96;67.71;68.93;80.59;73.01;69.79;60.83;53.36;54.61;54.81;59.92;50.04;48.94;62.96;57.8;46.19;57.75;57.13;49.81;43.5;43.4;55.88;40.84;65.66;56.89;46.67;63.34;73.27;55.73;72.79;81.27;78.13;53.35;53.36;67.44;85.04;83.94;80.24;75.08;80.91;92.47;95.29;66.27;86.27;85.89;76.79;74.83;68.94;64.69;63.22;62.17;76.74;81.06;97.47;101.76;111.47;80.06;85.7;86.9;100.06;92.74;88.17;88.07;103.59;88.55;95.45;66.43;98.12;97.74;82.01;80.05;96.22;92.97;92.53;76.73;79.45;95.46;80.78;74.04;77.34;78.56;76.34;68.76;77.09;68.32;57.34;74.01;72.09;54.55;63.82;59.57;76.07;75.02;76.73;81.05;88.39;85.14;90.98;75.18;69.12;85.13;76.58;59.84;80.29;72.53;107.39;79.13;63.54;72.02;111.25;86.47;70.84;84.92;56.7;77.87;63.14;60.85;31.87;55.43;57.15;51.22;55.44;93.56;45.96;52.45;118.16;101.42;92.54;84.78;110.06;81.8;64.83;63.73;84.03;78.87;59.48;71.04;97.72;79.98;84.18;82.58;79.17;89.81;114.03;78.77;95.64;118.59;96.56;96.41;68.01;76.49;73.35;48.57;48.58;62.66;49.64;48.54;44.84;39.68;45.51;57.07;96.79;67.77;87.77;87.39;78.29;76.33;62.66;58.41;56.94;55.89;70.46;74.78;73.86;95.03;86.04;83.75;44.79;68.35;103.75;86.01;66.06;64.46;89.98;100.62;99.23;70.21;71.28;70.9;84.29;82.33;55.31;67.54;78.92;54.62;91.52;76.91;72.73;66.8;59.69;97.81;43.21;49.7;96.34;61.08;43.01;65.96;66.26;66.11;83.67;79.42;65.3;64.25;102.86;107.18;55.26;67.49;85.15;60.85;80.68;66.07;81.4;80.09;90.95;96.97;119.87;77.94;87.98;92.27;122.7;91.29;102.94;104.14;89.8;110.97;75.83;73.54;58.34;81.9;69.63;61.88;87.54;105.01;65.18;51.26;111.29;109.98;93.54;99.56;110.85;68.92;79.61;72.29;72.1;72.0;81.92;66.88;105.41;87.67;83.15;81.55;91.92;102.56;114.82;79.77;118.08;106.66;92.4;83.53;101.17;105.46;115.17;83.76;89.4;90.6;84.83;77.51;72.94;72.84;88.36;73.32;105.27;76.25;107.94;107.56;91.83;89.87;103.48;100.23;99.79;83.99;86.71;102.72;73.78;94.95;85.96;83.67;44.71;68.27;115.36;97.62;77.67;76.07;101.59;112.23;90.43;61.41;62.48;62.1;75.49;73.53;60.29;72.52;83.9;59.6;96.5;81.89;80.15;72.4;86.73;104.2;71.25;57.33;103.76;68.71;72.08;60.66;80.58;71.71;110.71;107.46;94.37;78.57;97.56;113.57;57.73;69.96;99.31;75.01;74.43;59.82;68.01;80.89;85.34;81.7;87.16;53.52;74.59;67.85;91.87;93.09;112.52;104.94;84.19;78.26;45.0;83.12;60.14;66.63;63.57;55.82;64.41;81.88;50.34;36.42;91.62;104.5;81.65;78.01;81.44;47.8;59.94;51.17;44.57;61.24;78.94;61.4;93.52;58.26;55.62;78.57;81.16;81.01;86.62;51.57;79.09;67.67;61.7;52.83;98.57;91.83;95.13;96.35;94.13;86.55;82.23;73.46;62.48;79.15;77.23;59.69;85.23;80.98;97.48;96.43;98.14;102.46;117.57;114.32;120.16;104.36;98.3;114.31;70.67;64.74;57.63;95.75;41.15;47.64;112.25;76.99;58.92;81.87;82.17;82.02;62.1;57.85;43.73;42.68;81.29;85.61;58.31;70.54;88.2;63.9;83.73;69.12;75.62;67.87;82.2;99.67;66.72;52.8;105.51;70.46;73.83;62.41;82.33;73.46;95.39;92.14;79.05;63.25;82.24;98.25;50.7;62.93;92.28;67.98;67.4;52.79];
beta_W = [17.01;13.47;13.58;13.16;16.85;13.53;12.27;12.32;16.76;15.42;12.44;12.6;12.63;12.37;11.89;11.44;11.81;10.95;13.93;10.39;10.0;13.87;11.01;9.75;12.77;9.22;8.8;8.38;10.5;7.18;8.08;6.56;10.04;15.33;12.2;7.6;8.56;6.19;6.67;11.89;12.64;7.46;16.34;12.27;7.93;10.99;8.52;7.83;10.42;10.47;9.63;8.28;7.33;7.49;9.28;7.76;7.09;12.38;12.85;8.25;13.95;10.24;12.21;16.88;17.51;12.58;14.53;13.13;9.46;8.37;9.79;9.76;12.57;12.31;11.42;10.97;9.39;8.53;12.93;10.57;10.27;15.49;16.4;11.22;12.79;9.09;10.09;14.76;16.29;11.36;16.65;14.98;12.11;10.65;11.85;10.87;21.52;17.98;16.77;20.64;17.04;15.77;16.97;12.91;12.29;15.35;12.67;11.98;13.64;12.24;12.51;11.42;16.56;16.53;13.69;12.02;14.06;12.6;13.4;12.41;13.13;9.58;9.69;9.28;12.97;9.65;10.18;10.23;14.67;13.33;10.35;10.51;13.29;13.04;12.56;12.11;12.47;11.61;17.33;13.8;13.4;17.28;14.42;13.16;15.22;11.68;14.01;13.59;18.45;15.13;14.13;15.36;20.89;16.58;13.61;15.55;13.91;17.03;15.47;13.15;11.3;13.35;14.99;13.68;13.98;18.94;13.86;13.73;10.13;10.18;13.89;12.54;14.33;14.49;12.69;13.92;16.14;11.84;12.46;14.4;15.71;19.29;18.36;16.34;12.58;15.84;9.6;12.74;12.87;14.52;11.54;13.02;11.57;11.32;12.22;11.77;15.68;14.82;10.84;13.97;14.52;12.2;10.51;12.57;9.75;13.33;13.49;11.46;8.6;11.87;8.96;9.09;10.02;12.0;8.81;11.38;11.08;7.55;8.13;12.01;11.15;9.89;12.14;10.82;11.05;16.01;10.72;10.59;7.86;10.99;10.42;12.08;12.82;14.3;9.96;10.08;9.22;11.21;7.61;10.18;19.48;15.94;15.51;15.09;17.21;13.89;12.35;10.83;14.31;19.59;16.47;11.87;15.04;12.67;13.15;18.37;19.12;13.94;23.98;19.92;15.58;18.64;16.16;15.48;16.73;13.19;15.51;15.09;19.96;16.64;15.94;17.17;22.7;18.39;15.42;17.36;15.18;18.31;16.74;14.42;12.57;14.63;14.69;13.37;13.68;18.64;13.56;13.43;15.64;14.12;13.22;18.5;20.14;15.55;14.8;16.02;18.01;13.71;12.76;14.7;19.65;25.25;19.5;15.67;18.24;21.89;15.11;13.8;18.92;20.34;17.21;14.17;18.16;15.79;13.05;18.27;22.57;17.38;12.52;15.65;16.5;14.18;10.38;12.44;14.23;19.84;16.13;12.3;14.81;18.46;15.55;11.65;16.61;18.89;15.01;14.02;19.25;15.18;12.12;15.18;14.71;14.02;20.3;18.98;19.51;24.47;18.65;18.52;15.48;14.17;14.64;16.06;20.59;17.55;18.12;14.21;12.48;14.76;15.38;14.39;14.14;14.2;13.36;12.01;11.06;11.21;9.36;7.84;7.18;12.46;12.93;8.33;13.3;9.59;11.55;16.22;16.86;11.93;18.64;17.24;13.57;12.48;13.9;13.88;8.76;8.81;12.52;11.17;12.96;13.12;13.07;14.29;16.51;12.21;12.83;14.77;10.8;14.38;13.45;11.42;7.66;10.93;6.71;9.85;9.98;11.64;8.65;10.14;12.17;10.64;9.74;15.03;16.67;12.07;12.17;13.39;15.38;11.08;10.12;12.07;12.87;18.47;12.72;8.89;11.46;15.11;11.93;10.62;15.73;17.16;14.02;10.98;19.72;16.02;13.37;18.04;23.61;18.68;12.29;15.87;17.77;15.74;9.63;12.89;15.09;20.69;17.83;14.0;15.96;19.61;16.59;11.96;15.85;20.16;15.46;15.32;13.62;12.21;8.84;7.75;12.15;12.13;12.87;16.01;17.18;18.84;14.29;15.78;12.34;11.02;12.34;13.76;14.15;11.1;15.56;10.93;8.12;12.43;12.65;12.5;18.61;18.36;17.46;17.02;15.43;14.57;14.37;12.0;11.71;16.93;17.84;12.65;15.61;11.91;12.91;17.57;19.11;14.18;23.02;21.34;18.48;17.02;18.22;17.23;11.17;10.92;11.82;11.38;15.28;14.43;13.27;16.4;16.95;14.63;12.94;15.0;11.77;15.35;15.51;13.48;10.62;13.89;9.03;9.16;10.09;12.07;8.88;11.45;16.08;13.72;10.98;16.2;20.49;15.3;13.34;16.46;17.31;15.0;11.2;13.25;14.27;19.87;16.17;12.33;14.84;18.49;15.75;11.84;16.8;19.09;15.21;14.22;16.79;13.08;10.44;15.1;20.67;15.74;11.4;14.98;16.88;14.86;8.74;12.01;13.24;18.84;15.98;12.15;14.11;17.76;15.64;11.01;14.9;19.21;14.51;14.37;16.0;14.33;11.76;10.3;12.48;11.5;15.26;15.38;17.36;19.34;15.33;17.9;15.26;11.35;12.51;14.8;14.64;13.65;15.85;11.22;10.46;14.77;14.02;13.87;19.58;16.05;14.84;18.71;15.1;13.84;15.34;11.27;10.66;13.72;11.03;10.35;12.99;11.58;11.86;10.77;15.9;15.88;15.04;13.37;15.41;13.95;14.74;13.76;18.84;15.31;15.89;19.76;18.91;17.65;20.94;19.62;19.85;24.81;19.52;19.39;15.84;18.98;18.41;20.06;20.8;22.28;17.19;17.31;16.46;18.44;14.84;17.41;18.84;14.78;11.71;14.78;14.3;13.62;16.09;14.78;15.31;20.27;14.44;14.31;15.0;13.69;14.16;15.58;20.11;17.07;17.43;13.52;11.79;14.07;14.69;13.7;16.35;14.95;11.58;10.49;14.89;14.87;10.97;14.11;15.28;16.93;12.39;13.87;14.38;13.06;14.38;15.8;16.18;13.14;21.32;16.69;13.88;18.19;18.4;18.25;18.45;16.78;14.21;12.75;14.93;13.95;11.02;11.14;13.12;15.1;11.09;13.66;15.93;12.02;13.18;15.46;15.31;14.32;16.11;11.48;10.72;15.03;14.28;14.13];
mu_0 = [77.64;83.89;75.64;85.64;71.77;75.52;106.27;102.4;94.15;81.53;100.4;91.65;105.09;102.97;94.97;80.35;104.97;92.47;88.89;90.64;99.01;78.14;102.76;80.14;73.35;79.6;72.17;82.17;66.09;69.84;102.8;96.72;89.29;84.46;95.54;96.79;100.8;97.29;88.47;82.46;98.47;95.97;84.6;87.17;96.93;84.67;100.68;85.85;87.62;83.75;104.95;92.33;98.87;90.12;88.44;82.36;103.56;98.73;99.69;100.94;76.32;78.82;74.11;86.61;61.49;71.49;80.36;88.94;82.57;98.94;73.82;81.61;83.59;81.47;102.1;87.48;98.59;86.09;82.77;79.26;99.89;93.88;97.77;95.27;72.65;75.15;71.26;83.76;56.64;66.64;81.26;87.27;82.65;97.27;70.15;78.76;79.21;80.96;107.84;86.97;110.41;87.79;80.6;83.17;110.05;97.79;111.8;96.97;90.72;99.3;91.54;107.91;70.67;78.46;95.29;101.3;94.47;109.09;71.85;80.46;83.93;90.18;81.93;91.93;78.06;81.81;98.2;94.33;86.08;73.46;92.33;83.58;93.35;91.23;83.23;68.61;93.23;80.73;91.18;92.93;101.3;80.43;105.05;82.43;65.28;71.53;60.43;70.43;68.38;72.13;76.7;84.65;73.55;77.22;79.8;75.52;74.7;81.55;76.4;75.22;86.4;78.37;72.53;71.43;70.83;63.4;74.58;68.25;93.91;90.04;93.21;80.59;101.16;92.41;91.06;99.01;102.18;105.85;98.31;94.03;78.94;77.44;90.76;93.73;78.14;82.61;97.01;87.56;85.19;92.03;76.44;92.73;89.88;87.76;94.03;79.41;100.88;88.38;92.73;99.58;105.85;104.67;103.73;95.7;82.61;81.11;91.58;94.55;76.96;81.43;101.58;93.23;92.61;97.7;80.11;93.55;85.5;87.25;99.77;78.9;98.67;76.05;76.53;75.43;87.95;80.52;89.7;83.37;86.65;77.2;83.8;90.64;62.93;79.22;87.55;79.2;90.4;95.49;67.78;81.22;84.06;90.31;82.88;92.88;76.8;80.55;94.86;88.78;81.35;76.52;87.6;88.85;90.01;86.5;77.68;71.67;87.68;85.18;85.63;88.2;97.96;85.7;101.71;86.88;69.7;75.95;64.85;74.85;72.8;76.55;76.83;84.78;73.68;77.35;79.93;75.65;75.65;82.5;77.35;76.17;87.35;79.32;71.27;70.17;69.57;62.14;73.32;66.99;99.15;93.07;92.77;87.94;100.72;101.97;95.48;103.43;103.13;106.8;97.05;92.77;81.97;84.79;96.0;93.29;91.17;85.64;102.25;97.12;88.22;91.59;89.47;97.97;93.48;89.97;91.95;85.94;98.8;96.3;97.15;104.0;105.98;104.8;102.47;94.44;84.82;87.64;95.18;92.47;89.17;83.64;105.18;101.15;94.82;95.62;92.32;97.15;91.31;93.88;102.11;89.85;101.01;86.18;80.95;79.85;88.08;80.65;90.65;84.32;93.28;88.15;89.61;92.98;77.35;85.85;93.36;89.33;97.03;97.83;82.2;87.03;85.52;81.65;102.85;90.23;96.77;88.02;82.05;75.97;97.17;92.34;93.3;94.55;81.35;83.85;79.14;91.64;66.52;76.52;87.09;95.67;89.3;105.67;80.55;88.34;99.88;96.01;99.18;86.56;107.13;98.38;78.38;86.33;89.5;93.17;85.63;81.35;95.71;94.21;107.53;110.5;94.91;99.38;101.45;92.0;89.63;96.47;80.88;97.17;100.7;94.62;94.32;89.49;102.27;103.52;82.67;90.62;90.32;93.99;84.24;79.96;97.79;100.61;111.82;109.11;106.99;101.46;107.95;102.82;93.92;97.29;95.17;103.67;70.55;73.05;64.87;77.37;63.37;73.37;88.58;87.08;78.9;81.87;81.4;85.87;86.37;89.19;82.37;79.66;94.87;89.34;69.75;74.07;73.75;68.54;83.75;74.22;88.62;97.2;85.15;101.52;75.7;83.49;92.62;83.17;71.12;77.96;79.7;95.99;94.83;89.7;76.8;80.17;93.17;101.67;68.05;72.37;86.08;80.87;93.87;84.34;81.43;79.31;99.94;85.32;96.43;83.93;77.14;73.63;94.26;88.25;92.14;89.64;81.29;83.79;79.9;92.4;65.28;75.28;86.75;92.76;88.14;102.76;75.64;84.25;99.46;97.34;103.61;88.99;110.46;97.96;80.81;87.66;93.93;92.75;91.81;83.78;99.32;97.82;108.29;111.26;93.67;98.14;104.78;96.43;95.81;100.9;83.31;96.75;98.64;95.13;97.11;91.1;103.96;101.46;84.28;91.13;93.11;91.93;89.6;81.57;101.4;104.22;111.76;109.05;105.75;100.22;109.64;105.61;99.28;100.08;96.78;101.61;74.16;76.66;68.48;80.98;66.98;76.98;88.52;87.02;78.84;81.81;81.34;85.81;87.13;89.95;83.13;80.42;95.63;90.1;68.51;72.83;72.51;67.3;82.51;72.98;93.13;99.14;88.84;103.46;80.49;89.1;97.13;88.78;78.48;83.57;84.49;97.93;98.52;94.49;84.16;84.96;98.78;103.61;71.66;75.98;86.02;80.81;94.63;85.1;80.62;82.37;109.25;88.38;111.82;89.2;76.33;78.9;105.78;93.52;107.53;92.7;90.6;99.18;91.42;107.79;70.55;78.34;90.32;96.33;89.5;104.12;66.88;75.49;84.62;86.37;98.89;78.02;97.79;75.17;65.97;64.87;77.39;69.96;79.14;72.81;94.6;85.15;91.75;98.59;70.88;87.17;94.32;85.97;97.17;102.26;74.55;87.99;86.01;88.58;96.81;84.55;95.71;80.88;71.65;70.55;78.78;71.35;81.35;75.02;101.1;95.97;97.43;100.8;85.17;93.67;99.18;95.15;102.85;103.65;88.02;92.85;81.77;90.35;78.3;94.67;68.85;76.64;96.13;86.68;74.63;81.47;83.21;99.5;96.95;91.82;78.92;82.29;95.29;103.79;58.05;62.37;76.08;70.87;83.87;74.34;82.67;88.68;78.38;93.0;70.03;78.64;100.7;92.35;82.05;87.14;88.06;101.5;99.88;95.85;85.52;86.32;100.14;104.97;62.9;67.22;77.26;72.05;85.87;76.34];
lo = transpose(beta_W);
beta_W=1./beta_W;
betaprime = beta_W*lo;
%The simple function to run KGCB
covM = covMtemp*betaprime;
mu=mu*(-1);
mu_0=mu_0*(-1);
[mu_est, OC, choices, mu_estALL]=kgcb(mu,mu_0,beta_W,covM,N);
%{
%Plot the final estimates vs. truth
plot(x,mu,'-r','LineWidth',2); %'-r' makes it a red line, LineWidth is the thickness
hold on %hold the figure, as we'll also put on a second one
plot(x,mu_est,'.b','LineWidth',2); %'.b' makes it a blue dotted line
hold off

%adjust the axes and add legends
axis([1 100 min(mu)-0.5 max(mu)+0.5]);
legend('Truth','Estimate');

%Plot the estimate at the Kth time step vs. truth
K=10;

plot(x,mu,'-r','LineWidth',2); %'-r' makes it a red line, LineWidth is the thickness
hold on %hold the figure, as we'll also put on a second one
plot(x,mu_estALL(:,K),'.b','LineWidth',2); %'.b' makes it a blue dotted line
hold off

%adjust the axes and add legends
axis([1 100 min(mu)-0.5 max(mu)+0.5]);
legend('Truth','Estimate');

%Plot Opportunity Cost vs Time
plot(1:N,OC,'-g','LineWidth',1.5);
xlabel('Iteration');
ylabel('Opportunity Cost');

%or the log of it
semilogy(1:N,OC,'-g','LineWidth',1.5);
xlabel('Iteration');
ylabel('Log_{10}(Opportunity Cost)');
%}

