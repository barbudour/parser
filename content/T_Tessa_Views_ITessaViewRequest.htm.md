# ITessaViewRequest - интерфейс
Описание интерфейса запроса к представлению
[ITessaView](T_Tessa_Views_ITessaView.htm). Запрос содержит информацию
необходимую для осуществления вызова представления указанного в
[View](P_Tessa_Views_ITessaViewRequest_View.htm) с параметрами
[Values](P_Tessa_Views_ITessaViewRequest_Values.htm). Для получения из
представления результатов подмножества необходимо задать имя подмножества в
[SubsetName](P_Tessa_Views_ITessaViewRequest_SubsetName.htm). Значения
заданные в [SortingColumn](T_Tessa_Views_SortingColumn.htm) влияют на
сортировку результатов выполнения представления. Результат выполнения запроса
к представлению возвращается в виде объекта реализующего интерфейс
[ITessaViewResult](T_Tessa_Views_ITessaViewResult.htm)
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaViewRequest : IViewConnectionInfo
VB __Копировать
     Public Interface ITessaViewRequest
    	Inherits IViewConnectionInfo
C++ __Копировать
     public interface class ITessaViewRequest : IViewConnectionInfo
F# __Копировать
     type ITessaViewRequest = 
        interface
            interface IViewConnectionInfo
        end
Implements
    [IViewConnectionInfo](T_Tessa_Views_IViewConnectionInfo.htm)
##  __Свойства
[CalculateRowCounting](P_Tessa_Views_ITessaViewRequest_CalculateRowCounting.htm)|
Признак необходимости подсчета количества строк. Для подсчета строк
представление должно содержать подмножество осуществляющее подсчет количества
строк. Имя данного подмножества указывается в свойстве
[RowCountSubset](P_Tessa_Views_Metadata_IViewMetadata_RowCountSubset.htm)
метаданных представления.  
---|---  
[ConnectionAlias](P_Tessa_Views_IViewConnectionInfo_ConnectionAlias.htm)|
Алиас строки подключения (из конфигурационного файла веб сервиса `app.json`) к
БД, на которой будет выполняться представление вместо дефолтной базы. В
конфигурационном файле можно указать подключение к любой СУБД. Если, например,
основная база - MSSQL, а подключение к базе Postgres, то запрос генерируется
по правилам Postgres; если же база какая-то другая (например, Oracle), то по
умолчанию используются правила генерации для MSSQL.
С помощью данного параметра можно прописать подключение к другой базе, в том
числе не к базе Tessa, а, например, к какой-то другой информационнной системе.
Укажите null или пустую строку, если используется соединение по умолчанию.
Также на алиас соединения влияет одноимённая настройка в метаинформации
представления.
Для использования этой настройки требуется модуль лицензии "Кластеризация". Он
включён в лицензии Enterprise.
(Унаследован от [IViewConnectionInfo](T_Tessa_Views_IViewConnectionInfo.htm))  
[ExecutionTimeOut](P_Tessa_Views_ITessaViewRequest_ExecutionTimeOut.htm)|
Тайм-аут выполнения запроса. null \- используется значение по умолчанию
заданное в настройках системы. Отличное от null значение будет использовано
для выставления тайм-аута запроса. При этом если при выполнении запроса тайм-
аут истечет, то в результате будет возвращен результат выполнения запроса с
пустым списком строк и
[HasTimeOut](P_Tessa_Views_ITessaViewResult_HasTimeOut.htm) выставленным в
true.  
[SkipErrorLogging](P_Tessa_Views_ITessaViewRequest_SkipErrorLogging.htm)|
Возвращает или задаёт значение, показывающее, что не требуется создавать
карточку ошибки при ошибке выполнения представления.  
[SortingColumns](P_Tessa_Views_ITessaViewRequest_SortingColumns.htm)|  Список
колонок сортировки. В случае если колонки сортировки результатов выполнения
представления не указаны сортировка производится по
[DefaultSortColumn](P_Tessa_Views_Metadata_IViewMetadata_DefaultSortColumn.htm)
и
[DefaultSortDirection](P_Tessa_Views_Metadata_IViewMetadata_DefaultSortDirection.htm)
если они указаны для представления. В случае исполнения представления в режиме
подмножества сортировка не производится.  
[SubsetName](P_Tessa_Views_ITessaViewRequest_SubsetName.htm)|  Имя вызываемого
подмножества представления. Указывается в случае необходимости получения
данных подмножества представления
[View](P_Tessa_Views_ITessaViewRequest_View.htm)  
[Values](P_Tessa_Views_ITessaViewRequest_Values.htm)|  Список значений
параметров.  
[View](P_Tessa_Views_ITessaViewRequest_View.htm)|  Метаданные вызываемого
представления. На основании указанного значения будет осуществлен вызов
представления [Alias](P_Tessa_Views_Metadata_INamedViewMetadataItem_Alias.htm)  
[ViewAlias](P_Tessa_Views_ITessaViewRequest_ViewAlias.htm)|  Псевдоним
представления  
## __Методы расширения
[GetCriteriaName](M_Tessa_Views_TessaViewRequestHelper_GetCriteriaName.htm)|
Возвращает количество условий заданных для параметра paramName  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
---|---  
[GetParameterCriteriaCount](M_Tessa_Views_TessaViewRequestHelper_GetParameterCriteriaCount.htm)|
Возвращает количество условий заданных для параметра paramName  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[GetParameterFirstValue](M_Tessa_Views_TessaViewRequestHelper_GetParameterFirstValue.htm)|
Возвращает первое значение параметра заданного в запросе request для параметра
с именем paramName. Если значение не задано или количество значений меньше
одного то будет выдано исключение  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[GetParameterFirstValueIsNull](M_Tessa_Views_TessaViewRequestHelper_GetParameterFirstValueIsNull.htm)|
Возвращает признак того, что первое значение параметра, заданного в запросе
request для параметра с именем paramName, равно null. Если значение не задано
или количество значений меньше одного, то будет выдано исключение. Метод
учитывает операторы "пусто"
[IsNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNullCriteriaOperator.htm)
и "не пусто"
[IsNotNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNotNullCriteriaOperator.htm).  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[GetParameterSecondValue](M_Tessa_Views_TessaViewRequestHelper_GetParameterSecondValue.htm)|
Возвращает второе значение параметра заданного в запросе request для параметра
с именем paramName. Если значение не задано или количество значений меньше
одного то будет выдано исключение  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[GetParameterSingleIsNull](M_Tessa_Views_TessaViewRequestHelper_GetParameterSingleIsNull.htm)|
Возвращает признак того, что единственное значение параметра, заданного в
запросе request для параметра с именем paramName, равно null. Если значение не
задано или количество значений не равно одному, то будет выдано исключение.
Метод учитывает операторы "пусто"
[IsNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNullCriteriaOperator.htm)
и "не пусто"
[IsNotNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNotNullCriteriaOperator.htm).  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[GetParameterSingleValue](M_Tessa_Views_TessaViewRequestHelper_GetParameterSingleValue.htm)|
Возвращает единственное значение параметра заданного в запросе request для
параметра с именем paramName. Если значение не задано или количество значений
не равно одному то будет выдано исключение  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[GetParameterValueCount](M_Tessa_Views_TessaViewRequestHelper_GetParameterValueCount.htm)|
Возвращает число заданных значений параметра. Если параметр не задан или
условий больше чем 1 возвращает -1  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[IsAnySubsetDefined](M_Tessa_Views_TessaViewRequestHelper_IsAnySubsetDefined.htm)|
Осуществялет проверку необходимости работы в режиме подмножества  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[IsDefinedAllParametersOrSubset](M_Tessa_Views_Metadata_ViewRequestExtender_IsDefinedAllParametersOrSubset.htm)|
Осуществляет проверку наличия в коллекции параметра или имени сабсета  
(Определяется
[ViewRequestExtender](T_Tessa_Views_Metadata_ViewRequestExtender.htm))  
[IsDefinedParameter](M_Tessa_Views_TessaViewRequestHelper_IsDefinedParameter.htm)|
Определяет задан ли параметр с именем parameterName в запросе request  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[IsSubsetDefined](M_Tessa_Views_TessaViewRequestHelper_IsSubsetDefined.htm)|
Осуществляет проверку работы в режиме любого подмножеств заданного в параметре
subsetName  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[IterateParameterCriteriasAsync](M_Tessa_Views_TessaViewRequestHelper_IterateParameterCriteriasAsync.htm)|
Осуществляет выполнение метода operate над операциями заданным в параметре
parameterName, если он определен в запросе  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[RemovePredefinedParameters](M_Tessa_Views_TessaViewRequestHelper_RemovePredefinedParameters.htm)|
Удаляет из запроса request зарезервированные имена
[AdministratorPredefinedParam](F_Tessa_Views_Parser_SyntaxTree_Expressions_ExpressionConst_AdministratorPredefinedParam.htm)[SubsetPredefinedParam](F_Tessa_Views_Parser_SyntaxTree_Expressions_ExpressionConst_SubsetPredefinedParam.htm)[NormalPredefinedParam](F_Tessa_Views_Parser_SyntaxTree_Expressions_ExpressionConst_NormalPredefinedParam.htm)  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[SortDirection](M_Tessa_Views_TessaViewRequestHelper_SortDirection.htm)|
Получает порядок сортировки для столбца columnAlias в запросе request.
Возвращает строку "asc", если выполняется сортировка по возрастанию; строку
"desc", если выполняется сортировка по убыванию; или null, если сортировка по
столбцу не выполняется.  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[SortedBy](M_Tessa_Views_TessaViewRequestHelper_SortedBy.htm)|  Проверяет
наличие колонки columnAlias в списке колонок, по которым осуществляется
сортировка в запросе request  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
[TryGetParameter](M_Tessa_Views_TessaViewRequestHelper_TryGetParameter.htm)|
Возвращает параметр запроса к представлению по имени parameterName  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
