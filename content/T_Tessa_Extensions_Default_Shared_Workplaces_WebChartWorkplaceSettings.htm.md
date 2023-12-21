# WebChartWorkplaceSettings - класс
Настройки вывода диаграммы вместо представления в лёгком клиенте.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workplaces](N_Tessa_Extensions_Default_Shared_Workplaces.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class WebChartWorkplaceSettings : IStorageSerializable
VB __Копировать
    <SerializableAttribute>
    Public Class WebChartWorkplaceSettings
    	Implements IStorageSerializable
C++ __Копировать
    [SerializableAttribute]
    public ref class WebChartWorkplaceSettings : IStorageSerializable
F# __Копировать
     [<SerializableAttribute>]
    type WebChartWorkplaceSettings = 
        class
            interface IStorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebChartWorkplaceSettings
Implements
    [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Конструкторы
[WebChartWorkplaceSettings](M_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings__ctor.htm)|
Инициализирует новый экземпляр класса WebChartWorkplaceSettings  
---|---  
##  __Свойства
[Caption](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_Caption.htm)|
Название диаграммы.  
---|---  
[CaptionColumn](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_CaptionColumn.htm)|
Имя колонки с названием диаграммы.  
[ColumnCount](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_ColumnCount.htm)|
Кол-во столбцов диаграмм в строке  
[DiagramDirection](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_DiagramDirection.htm)|
Расположение диаграммы.  
[DiagramType](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_DiagramType.htm)|
Тип диаграммы.  
[DoesntShowZeroValues](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_DoesntShowZeroValues.htm)|
Не показывать нулевые значения.  
[LegendItemMinWidth](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_LegendItemMinWidth.htm)|
Минимальная ширина элемента в подписи к графику.  
[LegendNotWrap](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_LegendNotWrap.htm)|
Флаг запрещающий перенос слов на новую строку, если фраза не умещается в одну
строку.  
[LegendPosition](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_LegendPosition.htm)|
Положение подписи диаграммы.  
[PaletteTypeId](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_PaletteTypeId.htm)|
Идентификатор палитры цветов.  
[SelectedColor](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_SelectedColor.htm)|
Цвет выбора фрагмента диаграммы.  
[XColumn](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_XColumn.htm)|
Имя колонки, содержащей значения по оси X.  
[YColumn](P_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_YColumn.htm)|
Имя колонки, содержащей значения по оси Y.  
## __Методы
[Deserialize](M_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
---|---  
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
[Serialize](M_Tessa_Extensions_Default_Shared_Workplaces_WebChartWorkplaceSettings_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workplaces - пространство
имён](N_Tessa_Extensions_Default_Shared_Workplaces.htm)
