# TessaViewRequestHelper - класс
The tessa view request helper.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TessaViewRequestHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class TessaViewRequestHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class TessaViewRequestHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type TessaViewRequestHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaViewRequestHelper
##  __Методы
[AddValue(RequestCriteria,
CriteriaValue)](M_Tessa_Views_TessaViewRequestHelper_AddValue_1.htm)|
Добавляет новое значение в список  
---|---  
[AddValue(RequestCriteria, String,
Object)](M_Tessa_Views_TessaViewRequestHelper_AddValue.htm)|  Добавляет новое
значение в список  
[GetCriteriaName](M_Tessa_Views_TessaViewRequestHelper_GetCriteriaName.htm)|
Возвращает количество условий заданных для параметра paramName  
[GetParameterCriteriaCount](M_Tessa_Views_TessaViewRequestHelper_GetParameterCriteriaCount.htm)|
Возвращает количество условий заданных для параметра paramName  
[GetParameterFirstValue](M_Tessa_Views_TessaViewRequestHelper_GetParameterFirstValue.htm)|
Возвращает первое значение параметра заданного в запросе request для параметра
с именем paramName. Если значение не задано или количество значений меньше
одного то будет выдано исключение  
[GetParameterFirstValueIsNull](M_Tessa_Views_TessaViewRequestHelper_GetParameterFirstValueIsNull.htm)|
Возвращает признак того, что первое значение параметра, заданного в запросе
request для параметра с именем paramName, равно null. Если значение не задано
или количество значений меньше одного, то будет выдано исключение. Метод
учитывает операторы "пусто"
[IsNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNullCriteriaOperator.htm)
и "не пусто"
[IsNotNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNotNullCriteriaOperator.htm).  
[GetParameterSecondValue](M_Tessa_Views_TessaViewRequestHelper_GetParameterSecondValue.htm)|
Возвращает второе значение параметра заданного в запросе request для параметра
с именем paramName. Если значение не задано или количество значений меньше
одного то будет выдано исключение  
[GetParameterSingleIsNull](M_Tessa_Views_TessaViewRequestHelper_GetParameterSingleIsNull.htm)|
Возвращает признак того, что единственное значение параметра, заданного в
запросе request для параметра с именем paramName, равно null. Если значение не
задано или количество значений не равно одному, то будет выдано исключение.
Метод учитывает операторы "пусто"
[IsNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNullCriteriaOperator.htm)
и "не пусто"
[IsNotNullCriteriaOperator](T_Tessa_Views_Metadata_Criteria_IsNotNullCriteriaOperator.htm).  
[GetParameterSingleValue](M_Tessa_Views_TessaViewRequestHelper_GetParameterSingleValue.htm)|
Возвращает единственное значение параметра заданного в запросе request для
параметра с именем paramName. Если значение не задано или количество значений
не равно одному то будет выдано исключение  
[GetParameterValueCount](M_Tessa_Views_TessaViewRequestHelper_GetParameterValueCount.htm)|
Возвращает число заданных значений параметра. Если параметр не задан или
условий больше чем 1 возвращает -1  
[IsAnySubsetDefined](M_Tessa_Views_TessaViewRequestHelper_IsAnySubsetDefined.htm)|
Осуществялет проверку необходимости работы в режиме подмножества  
[IsDefinedParameter](M_Tessa_Views_TessaViewRequestHelper_IsDefinedParameter.htm)|
Определяет задан ли параметр с именем parameterName в запросе request  
[IsNull](M_Tessa_Views_TessaViewRequestHelper_IsNull.htm)|  Проверяет является
ли значение содержащееся в criteriaValuenull  
[IsSubsetDefined](M_Tessa_Views_TessaViewRequestHelper_IsSubsetDefined.htm)|
Осуществляет проверку работы в режиме любого подмножеств заданного в параметре
subsetName  
[IterateCriteriaValues](M_Tessa_Views_TessaViewRequestHelper_IterateCriteriaValues.htm)|
Осуществляет выполнение операции operate над условием criteria и значениями
заданным в нем  
[IterateParameterCriteriasAsync](M_Tessa_Views_TessaViewRequestHelper_IterateParameterCriteriasAsync.htm)|
Осуществляет выполнение метода operate над операциями заданным в параметре
parameterName, если он определен в запросе  
[RemovePredefinedParameters](M_Tessa_Views_TessaViewRequestHelper_RemovePredefinedParameters.htm)|
Удаляет из запроса request зарезервированные имена
[AdministratorPredefinedParam](F_Tessa_Views_Parser_SyntaxTree_Expressions_ExpressionConst_AdministratorPredefinedParam.htm)[SubsetPredefinedParam](F_Tessa_Views_Parser_SyntaxTree_Expressions_ExpressionConst_SubsetPredefinedParam.htm)[NormalPredefinedParam](F_Tessa_Views_Parser_SyntaxTree_Expressions_ExpressionConst_NormalPredefinedParam.htm)  
[SortDirection](M_Tessa_Views_TessaViewRequestHelper_SortDirection.htm)|
Получает порядок сортировки для столбца columnAlias в запросе request.
Возвращает строку "asc", если выполняется сортировка по возрастанию; строку
"desc", если выполняется сортировка по убыванию; или null, если сортировка по
столбцу не выполняется.  
[SortedBy](M_Tessa_Views_TessaViewRequestHelper_SortedBy.htm)|  Проверяет
наличие колонки columnAlias в списке колонок, по которым осуществляется
сортировка в запросе request  
[TryGetParameter](M_Tessa_Views_TessaViewRequestHelper_TryGetParameter.htm)|
Возвращает параметр запроса к представлению по имени parameterName  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
