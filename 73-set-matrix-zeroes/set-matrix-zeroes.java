class Solution {
    public void change(int row1,int col1,int[][] mat){
        for(int i=0;i<mat.length;i++){
        for(int j=0;j<mat[0].length;j++){
            mat[row1][j]=0;
            mat[i][col1]=0;
        }
      }
    }
    public void setZeroes(int[][] matrix) {
      int row=matrix.length;
      int col=matrix[0].length;
      int[][] mat=new int[row][col];
      for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            mat[i][j]=matrix[i][j];
        }
      }
      int row1=0,col1=0;
      for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            if(matrix[i][j]==0){
                row1=i;
                col1=j;
                change(row1,col1,mat);
            }
        }
      }
      for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            matrix[i][j]=mat[i][j];
        }
      }  
    }
}