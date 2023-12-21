# SharedNameFactory - класс
Фабрика, предоставляющая средства для создания глобальных имён, которые
возможно использовать для синхронизации между потоками и процессами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SharedNameFactory
VB __Копировать
     Public NotInheritable Class SharedNameFactory
C++ __Копировать
     public ref class SharedNameFactory sealed
F# __Копировать
     [<SealedAttribute>]
    type SharedNameFactory = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SharedNameFactory
##  __Конструкторы
[SharedNameFactory](M_Tessa_Platform_IPC_SharedNameFactory__ctor.htm)|
Создаёт экземпляр класса с указанием имени и типа экземпляров объектов, для
которых требуется синхронизация.  
---|---  
## __Свойства
[InstanceGroupName](P_Tessa_Platform_IPC_SharedNameFactory_InstanceGroupName.htm)|
Имя группы экземпляров класса, являющееся глобально уникальным для экземпляров
того же типа, расположенных в различных процессах, или null, если экземпляры
не сгруппированы.  
---|---  
[InstanceName](P_Tessa_Platform_IPC_SharedNameFactory_InstanceName.htm)|  Имя
экземпляра класса, являющееся глобально уникальным для экземпляров того же
типа, расположенных в различных процессах.  
[InstanceType](P_Tessa_Platform_IPC_SharedNameFactory_InstanceType.htm)| Тип
объекта, используемый для синхронизации экземпляров между потоками и
процессами.  
##  __Методы
[Create](M_Tessa_Platform_IPC_SharedNameFactory_Create.htm)|  Создаёт имя,
которое может использоваться для создания глобальных объектов синхронизации.  
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
##  __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
