# SharedEventArgs - класс
Базовый класс для аргументов события, разделяемых между процессами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SharedEventArgs : ISharedEventArgs, 
    	IBinarySerializable
VB __Копировать
     Public Class SharedEventArgs
    	Implements ISharedEventArgs, IBinarySerializable
C++ __Копировать
     public ref class SharedEventArgs : ISharedEventArgs, 
    	IBinarySerializable
F# __Копировать
     type SharedEventArgs = 
        class
            interface ISharedEventArgs
            interface IBinarySerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SharedEventArgs
Derived
[Tessa.Cards.Caching.CardCacheEventArgs](T_Tessa_Cards_Caching_CardCacheEventArgs.htm)
[Tessa.Views.AccessCacheSharedEventArgs](T_Tessa_Views_AccessCacheSharedEventArgs.htm)
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [ISharedEventArgs](T_Tessa_Platform_IPC_ISharedEventArgs.htm)
##  __Конструкторы
[SharedEventArgs](M_Tessa_Platform_IPC_SharedEventArgs__ctor.htm)|
Инициализирует новый экземпляр класса SharedEventArgs  
---|---  
##  __Методы
[Deserialize](M_Tessa_Platform_IPC_SharedEventArgs_Deserialize.htm)|
Десериализует объект из бинарной формы.  
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
[Serialize](M_Tessa_Platform_IPC_SharedEventArgs_Serialize.htm)| Сериализует
объект в бинарной форме.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[Empty](F_Tessa_Platform_IPC_SharedEventArgs_Empty.htm)|  Объект,
соответствующий событию без аргументов.  
---|---  
## __Методы расширения
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