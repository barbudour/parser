# TessaViewRequest - класс
Запрос к представлению.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class TessaViewRequest : StorageSerializable, 
    	ITessaViewRequest, IViewConnectionInfo
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class TessaViewRequest
    	Inherits StorageSerializable
    	Implements ITessaViewRequest, IViewConnectionInfo
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class TessaViewRequest : public StorageSerializable, 
    	ITessaViewRequest, IViewConnectionInfo
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type TessaViewRequest = 
        class
            inherit StorageSerializable
            interface ITessaViewRequest
            interface IViewConnectionInfo
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ TessaViewRequest
Implements
    [ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm), [IViewConnectionInfo](T_Tessa_Views_IViewConnectionInfo.htm)
##  __Конструкторы
[TessaViewRequest()](M_Tessa_Views_TessaViewRequest__ctor.htm)|  Конструктор
по умолчанию для сериализации. Не используйте для создания объекта.  
Устарело.  
---|---  
[TessaViewRequest(ITessaViewRequest)](M_Tessa_Views_TessaViewRequest__ctor_1.htm)|
Создаёт неглубокую копию заданного объекта
[ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm). Копируются
коллекции, но не содержащиеся в них объекты.  
[TessaViewRequest(IViewMetadata)](M_Tessa_Views_TessaViewRequest__ctor_2.htm)|
Инициализирует новый экземпляр класса TessaViewRequest.  
## __Свойства
[CalculateRowCounting](P_Tessa_Views_TessaViewRequest_CalculateRowCounting.htm)|
Признак необходимости подсчета количества строк. Для подсчета строк
представление должно содержать подмножество осуществляющее подсчет количества
строк. Имя данного подмножества указывается в свойстве
[RowCountSubset](P_Tessa_Views_Metadata_IViewMetadata_RowCountSubset.htm)
метаданных представления.  
---|---  
[ConnectionAlias](P_Tessa_Views_TessaViewRequest_ConnectionAlias.htm)|
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
[ExecutionTimeOut](P_Tessa_Views_TessaViewRequest_ExecutionTimeOut.htm)|
Тайм-аут выполнения запроса. null \- используется значение по умолчанию
заданное в настройках системы. Отличное от null значение будет использовано
для выставления тайм-аута запроса. При этом если при выполнении запроса тайм-
аут истечет, то в результате будет возвращен результат выполнения запроса с
пустым списком строк и
[HasTimeOut](P_Tessa_Views_ITessaViewResult_HasTimeOut.htm) выставленным в
true.  
[SkipErrorLogging](P_Tessa_Views_TessaViewRequest_SkipErrorLogging.htm)|
Возвращает или задаёт значение, показывающее, что не требуется создавать
карточку ошибки при ошибке выполнения представления.  
[SortingColumns](P_Tessa_Views_TessaViewRequest_SortingColumns.htm)|  Список
колонок сортировки. В случае если колонки сортировки результатов выполнения
представления не указаны сортировка производится по
[DefaultSortColumn](P_Tessa_Views_Metadata_IViewMetadata_DefaultSortColumn.htm)
и
[DefaultSortDirection](P_Tessa_Views_Metadata_IViewMetadata_DefaultSortDirection.htm)
если они указаны для представления. В случае исполнения представления в режиме
подмножества сортировка не производится.  
[SubsetName](P_Tessa_Views_TessaViewRequest_SubsetName.htm)|  Имя вызываемого
подмножества представления. Указывается в случае необходимости получения
данных подмножества представления
[View](P_Tessa_Views_ITessaViewRequest_View.htm)  
[Values](P_Tessa_Views_TessaViewRequest_Values.htm)|  Список значений
параметров.  
[View](P_Tessa_Views_TessaViewRequest_View.htm)|  Метаданные вызываемого
представления. На основании указанного значения будет осуществлен вызов
представления [Alias](P_Tessa_Views_Metadata_INamedViewMetadataItem_Alias.htm)  
[ViewAlias](P_Tessa_Views_TessaViewRequest_ViewAlias.htm)|  Псевдоним
представления  
## __Методы
[Deserialize](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
---|---  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Views_TessaViewRequest_DeserializeCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnSerialized](M_Tessa_Views_TessaViewRequest_OnSerialized.htm)|  Выполняется
после сериализации объекта  
[OnSerializing](M_Tessa_Views_TessaViewRequest_OnSerializing.htm)|
Выполняется при сериализации объекта  
[Serialize](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Views_TessaViewRequest_SerializeCore.htm)| Выполняет
сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetCriteriaName](M_Tessa_Views_TessaViewRequestHelper_GetCriteriaName.htm)|
Возвращает количество условий заданных для параметра paramName  
(Определяется
[TessaViewRequestHelper](T_Tessa_Views_TessaViewRequestHelper.htm))  
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
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[RepairParametersValuesType](M_Tessa_Web_Client_Helpers_CommonExtensions_RepairParametersValuesType.htm)|  
(Определяется
[CommonExtensions](T_Tessa_Web_Client_Helpers_CommonExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
