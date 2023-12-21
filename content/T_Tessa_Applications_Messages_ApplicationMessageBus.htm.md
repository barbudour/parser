# ApplicationMessageBus - класс
The application message bus.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationMessageBus : IApplicationMessageBus, 
    	IAsyncDisposable, IDisposable
VB __Копировать
     Public NotInheritable Class ApplicationMessageBus
    	Implements IApplicationMessageBus, IAsyncDisposable, IDisposable
C++ __Копировать
     public ref class ApplicationMessageBus sealed : IApplicationMessageBus, 
    	IAsyncDisposable, IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ApplicationMessageBus = 
        class
            interface IApplicationMessageBus
            interface IAsyncDisposable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationMessageBus
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IApplicationMessageBus](T_Tessa_Applications_Messages_IApplicationMessageBus.htm)
##  __Конструкторы
[ApplicationMessageBus](M_Tessa_Applications_Messages_ApplicationMessageBus__ctor.htm)|
Initializes a new instance of the ApplicationMessageBus class. Инициализирует
новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Методы
[Dispose](M_Tessa_Applications_Messages_ApplicationMessageBus_Dispose.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync](M_Tessa_Applications_Messages_ApplicationMessageBus_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[ProcessMessageAsync](M_Tessa_Applications_Messages_ApplicationMessageBus_ProcessMessageAsync.htm)|
Осуществляет обработку сообщения  
[RegisterAsync](M_Tessa_Applications_Messages_ApplicationMessageBus_RegisterAsync.htm)|
Выполняет регистрацию шины обработки сообщений в Tessa Applications  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnregisterAsync](M_Tessa_Applications_Messages_ApplicationMessageBus_UnregisterAsync.htm)|
Выполняет отмену регистрации приложения  
## __События
[MessageReceived](E_Tessa_Applications_Messages_ApplicationMessageBus_MessageReceived.htm)|
Событие, возникающее при получении сообщения  
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
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
