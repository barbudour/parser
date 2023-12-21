# TessaViewResult - класс
Результат выполнения запроса
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class TessaViewResult : ITessaViewResult
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class TessaViewResult
    	Implements ITessaViewResult
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class TessaViewResult : ITessaViewResult
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type TessaViewResult = 
        class
            interface ITessaViewResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaViewResult
Implements
    [ITessaViewResult](T_Tessa_Views_ITessaViewResult.htm)
##  __Конструкторы
[TessaViewResult](M_Tessa_Views_TessaViewResult__ctor.htm)|  Initializes a new
instance of the TessaViewResult class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Свойства
[Columns](P_Tessa_Views_TessaViewResult_Columns.htm)|  Gets or sets список
колонок  
---|---  
[DataTypes](P_Tessa_Views_TessaViewResult_DataTypes.htm)|  Gets or sets список
типов данных sql  
[HasTimeOut](P_Tessa_Views_TessaViewResult_HasTimeOut.htm)|  Gets or sets a
value indicating whether Признак прерывания выполнения запроса по тайм-ауту  
[Result](P_Tessa_Views_TessaViewResult_Result.htm)|  Gets or sets Колонки
представления  
[RowCount](P_Tessa_Views_TessaViewResult_RowCount.htm)|  Gets or sets
Количество строк, которое доступно в запросе. Данное количество, строк
является расчетным и не всегда равно количеству строк в
[Rows](P_Tessa_Views_ITessaViewResult_Rows.htm).  
[Rows](P_Tessa_Views_TessaViewResult_Rows.htm)|  Gets or sets список строк  
[SchemeTypes](P_Tessa_Views_TessaViewResult_SchemeTypes.htm)|  Список типов
данных.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetColumnIndex](M_Tessa_Views_TessaViewResult_GetColumnIndex.htm)|
Возвращает индекс колонки заданной параметром columnName или -1 если колонка
не найдена  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[ColumnsKey](F_Tessa_Views_TessaViewResult_ColumnsKey.htm)|  Ключ коллекции
содержащий имена столбцов  
---|---  
[DataTypesKey](F_Tessa_Views_TessaViewResult_DataTypesKey.htm)|  Ключ
коллекции содержащий названия типов данных в SQL-формате  
[RowCountKey](F_Tessa_Views_TessaViewResult_RowCountKey.htm)|  Ключ коллекции
содержащий расчетное количество строк  
[RowsKey](F_Tessa_Views_TessaViewResult_RowsKey.htm)|  Ключ коллекции
содержащий строки данных  
[SchemeTypesKey](F_Tessa_Views_TessaViewResult_SchemeTypesKey.htm)|  Ключ
коллекции содержащий типы данных в формате схемы данных  
## __Методы расширения
[ConvertDateTimeToLocal](M_Tessa_Views_TessaViewResultHelper_ConvertDateTimeToLocal.htm)|
Осуществляет пробразование данных DateTime в локальное время  
(Определяется
[TessaViewResultHelper](T_Tessa_Views_TessaViewResultHelper.htm))  
---|---  
[ConvertToListViewModel](M_Tessa_UI_Views_TessaListViewHelper_ConvertToListViewModel_2.htm)|
Преобразует результат запроса к представлению в модель таблицы
[ITessaListViewViewModel](T_Tessa_UI_Controls_TessaGrid_ITessaListViewViewModel.htm)  
(Определяется [TessaListViewHelper](T_Tessa_UI_Views_TessaListViewHelper.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
