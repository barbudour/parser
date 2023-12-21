# CommandDispatcher - класс
Диспетчер команд
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CommandDispatcher : ICommandDispatcher
VB __Копировать
     Public NotInheritable Class CommandDispatcher
    	Implements ICommandDispatcher
C++ __Копировать
     public ref class CommandDispatcher sealed : ICommandDispatcher
F# __Копировать
     [<SealedAttribute>]
    type CommandDispatcher = 
        class
            interface ICommandDispatcher
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CommandDispatcher
Implements
    [ICommandDispatcher](T_Tessa_Views_MessageServices_ICommandDispatcher.htm)
##  __Конструкторы
[CommandDispatcher](M_Tessa_Views_MessageServices_CommandDispatcher__ctor.htm)|
Инициализирует новый экземпляр класса CommandDispatcher  
---|---  
##  __Методы
[Deregister<TCommand>](M_Tessa_Views_MessageServices_CommandDispatcher_Deregister__1.htm)|
Осуществляет удаление регистрации обработчика команды  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync](M_Tessa_Views_MessageServices_CommandDispatcher_ExecuteAsync.htm)|
Вызывает исполнение команды  
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
[IsRegistered<TCommand>](M_Tessa_Views_MessageServices_CommandDispatcher_IsRegistered__1.htm)|
Осуществляет проверку наличия обработчика для команды  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Register](M_Tessa_Views_MessageServices_CommandDispatcher_Register.htm)|
Осуществляет регистрацию обработчика команды  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetHandler<TCommand>](M_Tessa_Views_MessageServices_CommandDispatcher_TryGetHandler__1.htm)|
Осуществляет попытку получения обработчика для команды TCommand  
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
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)
