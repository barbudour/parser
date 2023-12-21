# Registry<TItem> \- класс
Обобщенный класс реестра для объектов поддерживающих идентификацию с помощью
реализации интерфейса
[ITypeIdentifier](T_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_ITypeIdentifier.htm).
Заполнение реестра осуществляется через передачу списка объектов содержащийхся
в реестре через конструктор
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workplaces.WebChart.Palette](N_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class Registry<TItem> : IRegistry<TItem>
    where TItem : class, ITypeIdentifier
VB __Копировать
     Public Class Registry(Of TItem As {Class, ITypeIdentifier})
    	Implements IRegistry(Of TItem)
C++ __Копировать
    generic<typename TItem>
    where TItem : ref class, ITypeIdentifier
    public ref class Registry : IRegistry<TItem>
F# __Копировать
     type Registry<'TItem when 'TItem : not struct and ITypeIdentifier> = 
        class
            interface IRegistry<'TItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Registry<TItem>
Derived
[Tessa.Extensions.Default.Client.Workplaces.WebChart.Palette.Palettes](T_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_Palettes.htm)
Implements
    [IRegistry](T_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_IRegistry_1.htm)<TItem>
#### Параметры типа
TItem
     Тип элемента реестра 
## __Конструкторы
[Registry<TItem>](M_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_Registry_1__ctor.htm)|
Initializes a new instance of the Registry<TItem> class. Инициализирует новый
экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Свойства
[Items](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_Registry_1_Items.htm)|
Gets Список объектов реестра  
---|---  
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
[TryGetItem](M_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_Registry_1_TryGetItem.htm)|
Осуществляет поиск объекта по его идентификатору. В случае если объект с
указанным идентификатором не найден в реестре возвращает null  
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
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workplaces.WebChart.Palette - пространство
имён](N_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette.htm)
