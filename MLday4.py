{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled6.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNPCGjKN8GuNprypJLXuZyc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/abrishwon21/python/blob/master/MLday4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eur6SLXz8Dsu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "outputId": "570c8256-aa64-4ff3-c747-4c748be7ed01"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "d={'c1':[100,200,300],'c3':[500,600,700],'c4':[1100,6100,1700]}\n",
        "df_college_sort=pd.DataFrame(d,index=[2016,2012,2020])\n",
        "df_college_sort=df_college_sort.sort_index()\n",
        "df_college_sort"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>c1</th>\n",
              "      <th>c3</th>\n",
              "      <th>c4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2012</th>\n",
              "      <td>200</td>\n",
              "      <td>600</td>\n",
              "      <td>6100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2016</th>\n",
              "      <td>100</td>\n",
              "      <td>500</td>\n",
              "      <td>1100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020</th>\n",
              "      <td>300</td>\n",
              "      <td>700</td>\n",
              "      <td>1700</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       c1   c3    c4\n",
              "2012  200  600  6100\n",
              "2016  100  500  1100\n",
              "2020  300  700  1700"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Oi-w8NHX9gH2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l6TzzD4-8U9-",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "outputId": "06db310a-2525-42c8-8f9d-9d4b1fbba39e"
      },
      "source": [
        "df_college_sort=df_college_sort.sort_index(axis=1,ascending=False)\n",
        "df_college_sort"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>c4</th>\n",
              "      <th>c3</th>\n",
              "      <th>c1</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2012</th>\n",
              "      <td>6100</td>\n",
              "      <td>600</td>\n",
              "      <td>200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2016</th>\n",
              "      <td>1100</td>\n",
              "      <td>500</td>\n",
              "      <td>100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020</th>\n",
              "      <td>1700</td>\n",
              "      <td>700</td>\n",
              "      <td>300</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "        c4   c3   c1\n",
              "2012  6100  600  200\n",
              "2016  1100  500  100\n",
              "2020  1700  700  300"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6IftYaCT8kVS",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "outputId": "adeefc21-fded-4e18-8426-d6e7065039e1"
      },
      "source": [
        "#get index\n",
        "print('index of given data frame is')\n",
        "df_college_sort.index\n"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "index of given data frame is\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Int64Index([2012, 2016, 2020], dtype='int64')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jRzV-Lyz9htt",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 245
        },
        "outputId": "c04dbdcd-daa3-4f78-8355-b328a1ea3c1c"
      },
      "source": [
        "#sort value (by)\n",
        "print('_____Dataframe is__________')\n",
        "print(df_college_sort)\n",
        "print(\"after sort by value\")\n",
        "newD=df_college_sort.sort_values(by=['c3'],axis=0)\n",
        "newD"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "_____Dataframe is__________\n",
            "        c4   c3   c1\n",
            "2012  6100  600  200\n",
            "2016  1100  500  100\n",
            "2020  1700  700  300\n",
            "after sort by value\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>c4</th>\n",
              "      <th>c3</th>\n",
              "      <th>c1</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2016</th>\n",
              "      <td>1100</td>\n",
              "      <td>500</td>\n",
              "      <td>100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2012</th>\n",
              "      <td>6100</td>\n",
              "      <td>600</td>\n",
              "      <td>200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2020</th>\n",
              "      <td>1700</td>\n",
              "      <td>700</td>\n",
              "      <td>300</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "        c4   c3   c1\n",
              "2016  1100  500  100\n",
              "2012  6100  600  200\n",
              "2020  1700  700  300"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "h1StNUB6_gDf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 293
        },
        "outputId": "6fd51c64-0b5a-4a14-f05c-b809ed02f846"
      },
      "source": [
        "#fillna\n",
        "import pandas as pd\n",
        "\n",
        "'''\n",
        "syntax:\n",
        "df_fillmerged=df_merge.fillna(method='ffill')\n",
        "ffill method fills in forward,means whatever in previous will be filled in place of NaN\n",
        "for backward fill use bfill method\n",
        "to fill all NaN with uservalue\n",
        "df_merge.fillna(value=np.mean(df_merge['pprice']))\n",
        "or\n",
        "df_merge.fillna(value={'pname':'No Data','pprice':np.mean(df_merge['pprice']),'pcolor':'No color'})\n",
        "'''\n",
        "d1={'pid':[100,200,300],'pname':['mobile','watch','camera']}\n",
        "d2={'pid':[100,300,400],'pcolor':['golder','black','red']}\n",
        "df_left=pd.DataFrame(d1)\n",
        "df_right=pd.DataFrame(d2)\n",
        "ld=[['a','b','c'],[21,32,34]]\n",
        "dl2=pd.DataFrame(ld)\n",
        "\n",
        "##############3\n",
        "print(\"after outer merge\")\n",
        "douter=pd.merge(df_left,df_right,how='outer',on='pid')\n",
        "print(douter)\n",
        "\n",
        "newData=douter.fillna(method='ffill')\n",
        "newData\n",
        "\n",
        "print(\"after replacing with my value\")\n",
        "newData2=douter.fillna(value={'pid':'no id','pname':'No name','pcolor':'not given'})\n",
        "newData2\n",
        "\n",
        "\n"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "after outer merge\n",
            "   pid   pname  pcolor\n",
            "0  100  mobile  golder\n",
            "1  200   watch     NaN\n",
            "2  300  camera   black\n",
            "3  400     NaN     red\n",
            "after replacing with my value\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>pid</th>\n",
              "      <th>pname</th>\n",
              "      <th>pcolor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>100</td>\n",
              "      <td>mobile</td>\n",
              "      <td>golder</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>200</td>\n",
              "      <td>watch</td>\n",
              "      <td>not given</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>300</td>\n",
              "      <td>camera</td>\n",
              "      <td>black</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>400</td>\n",
              "      <td>No name</td>\n",
              "      <td>red</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   pid    pname     pcolor\n",
              "0  100   mobile     golder\n",
              "1  200    watch  not given\n",
              "2  300   camera      black\n",
              "3  400  No name        red"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TypBbgEtGzXI",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 263
        },
        "outputId": "a4e1c6e8-0ef1-46a4-8495-d0056346b451"
      },
      "source": [
        "ipl={'Team':['kkr','CSk','CSk','MI','MI','RR','CSk'],'Rank':[1,2,1,3,1,3,1],'Year':[2012,2012,2014,2015,2016,2014,2012]}\n",
        "df_ipl=pd.DataFrame(ipl)\n",
        "df_ipl"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Team</th>\n",
              "      <th>Rank</th>\n",
              "      <th>Year</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>kkr</td>\n",
              "      <td>1</td>\n",
              "      <td>2012</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>CSk</td>\n",
              "      <td>2</td>\n",
              "      <td>2012</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>CSk</td>\n",
              "      <td>1</td>\n",
              "      <td>2014</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>MI</td>\n",
              "      <td>3</td>\n",
              "      <td>2015</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>MI</td>\n",
              "      <td>1</td>\n",
              "      <td>2016</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>RR</td>\n",
              "      <td>3</td>\n",
              "      <td>2014</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>CSk</td>\n",
              "      <td>1</td>\n",
              "      <td>2012</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Team  Rank  Year\n",
              "0  kkr     1  2012\n",
              "1  CSk     2  2012\n",
              "2  CSk     1  2014\n",
              "3   MI     3  2015\n",
              "4   MI     1  2016\n",
              "5   RR     3  2014\n",
              "6  CSk     1  2012"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3Z8S4wqAH7yp",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        },
        "outputId": "5058699e-12a0-4d6d-8c72-0e07e20c2760"
      },
      "source": [
        "#now to groupby(key)=>groupby([key1,key2...])\n",
        "df_teambyT=df_ipl.groupby('Team')\n",
        "df_teambyT.groups"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'CSk': Int64Index([1, 2, 6], dtype='int64'),\n",
              " 'MI': Int64Index([3, 4], dtype='int64'),\n",
              " 'RR': Int64Index([5], dtype='int64'),\n",
              " 'kkr': Int64Index([0], dtype='int64')}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ejFbd8qKIor2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        },
        "outputId": "446c4983-2176-4614-ce6b-119bf67bb056"
      },
      "source": [
        "#grouby multiple key\n",
        "\n",
        "df_year=df_ipl.groupby(['Year'])\n",
        "df_year.groups\n"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{2012: Int64Index([0, 1, 6], dtype='int64'),\n",
              " 2014: Int64Index([2, 5], dtype='int64'),\n",
              " 2015: Int64Index([3], dtype='int64'),\n",
              " 2016: Int64Index([4], dtype='int64')}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w2cPg_aWJBLz",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 277
        },
        "outputId": "8fd08444-aac4-4304-ad21-865901b40e55"
      },
      "source": [
        "for n,group in df_year:\n",
        "  print(n)\n",
        "  print(group)\n",
        "  #to access the group get_group(key)"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2012\n",
            "  Team  Rank  Year\n",
            "0  kkr     1  2012\n",
            "1  CSk     2  2012\n",
            "6  CSk     1  2012\n",
            "2014\n",
            "  Team  Rank  Year\n",
            "2  CSk     1  2014\n",
            "5   RR     3  2014\n",
            "2015\n",
            "  Team  Rank  Year\n",
            "3   MI     3  2015\n",
            "2016\n",
            "  Team  Rank  Year\n",
            "4   MI     1  2016\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sGxTDzDcJncE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 158
        },
        "outputId": "dcce6eab-f883-4e2c-8717-95f2073b9879"
      },
      "source": [
        "#to access the group get_group(key)\n",
        "dfYear=df_ipl.groupby(['Year'])\n",
        "key=int(input(\"enter the year\"))\n",
        "dfYear.get_group(key)"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "enter the year2012\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Team</th>\n",
              "      <th>Rank</th>\n",
              "      <th>Year</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>kkr</td>\n",
              "      <td>1</td>\n",
              "      <td>2012</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>CSk</td>\n",
              "      <td>2</td>\n",
              "      <td>2012</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>CSk</td>\n",
              "      <td>1</td>\n",
              "      <td>2012</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Team  Rank  Year\n",
              "0  kkr     1  2012\n",
              "1  CSk     2  2012\n",
              "6  CSk     1  2012"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gUo6RRjTKqXi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "outputId": "044c189c-e8b1-4d67-d5ff-fc56aa0dc2e6"
      },
      "source": [
        "#aggregaition\n",
        "import numpy as np\n",
        "\n",
        "dfYear['Rank'].agg(np.mean)"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Year\n",
              "2012    1.333333\n",
              "2014    2.000000\n",
              "2015    3.000000\n",
              "2016    1.000000\n",
              "Name: Rank, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BtB6ZlvMK_T3",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 202
        },
        "outputId": "dda2bace-6cd0-4ffe-9e94-07d49d94cc9f"
      },
      "source": [
        "\n",
        "dfYear['Rank'].agg([np.mean,np.sum,np.std])\n",
        "  "
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>mean</th>\n",
              "      <th>sum</th>\n",
              "      <th>std</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Year</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2012</th>\n",
              "      <td>1.333333</td>\n",
              "      <td>4</td>\n",
              "      <td>0.577350</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2014</th>\n",
              "      <td>2.000000</td>\n",
              "      <td>4</td>\n",
              "      <td>1.414214</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2015</th>\n",
              "      <td>3.000000</td>\n",
              "      <td>3</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2016</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          mean  sum       std\n",
              "Year                         \n",
              "2012  1.333333    4  0.577350\n",
              "2014  2.000000    4  1.414214\n",
              "2015  3.000000    3       NaN\n",
              "2016  1.000000    1       NaN"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lbweBSGVNc_s",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 202
        },
        "outputId": "de512788-9371-47e3-ba3d-7cf5202520d3"
      },
      "source": [
        "path=\"/content/sample_data/Movie_Id_Titles\"\n",
        "path2=\"/content/sample_data/u.data\"\n",
        "df_movietable=pd.read_csv(path)\n",
        "df_user=pd.read_csv(path2)\n",
        "#mergedData=pd.merge(df_user,df_movietable,how=\"inner\",on=['item_id'])\n",
        "#mergedData\n",
        "df_movietable.head()"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>item_id</th>\n",
              "      <th>title</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Toy Story (1995)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>GoldenEye (1995)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>Four Rooms (1995)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>Get Shorty (1995)</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>Copycat (1995)</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   item_id              title\n",
              "0        1   Toy Story (1995)\n",
              "1        2   GoldenEye (1995)\n",
              "2        3  Four Rooms (1995)\n",
              "3        4  Get Shorty (1995)\n",
              "4        5     Copycat (1995)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 43
        }
      ]
    }
  ]
}