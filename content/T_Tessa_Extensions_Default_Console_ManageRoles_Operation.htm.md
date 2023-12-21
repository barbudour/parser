# Operation - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Console.ManageRoles](N_Tessa_Extensions_Default_Console_ManageRoles.htm)  
 **Сборка:** Tessa.Extensions.Default.Console (в
Tessa.Extensions.Default.Console.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Operation : ConsoleOperation<OperationContext>
VB __Копировать
     Public NotInheritable Class Operation
    	Inherits ConsoleOperation(Of OperationContext)
C++ __Копировать
     public ref class Operation sealed : public ConsoleOperation<OperationContext^>
F# __Копировать
     [<SealedAttribute>]
    type Operation = 
        class
            inherit ConsoleOperation<OperationContext>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ConsoleOperation](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm)<[OperationContext](T_Tessa_Extensions_Default_Console_ManageRoles_OperationContext.htm)> __ Operation
##  __Конструкторы
[Operation](M_Tessa_Extensions_Default_Console_ManageRoles_Operation__ctor.htm)|
Инициализирует новый экземпляр класса Operation  
---|---  
##  __Свойства
[ExtendedInitialization](P_Tessa_Platform_ConsoleApps_ConsoleOperation_1_ExtendedInitialization.htm)|
Признак того, что используется расширенная инициализация при открытии сессии
(с выполняемыми расширениями и стримом инициализации).  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
---|---  
[Logger](P_Tessa_Platform_ConsoleApps_ConsoleOperation_1_Logger.htm)|  Логгер
приложения.  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
[SessionManager](P_Tessa_Platform_ConsoleApps_ConsoleOperation_1_SessionManager.htm)|
Объект для управления клиентскими сессиями.  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
##  __Методы
[CheckDisposed](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
---|---  
[CloseAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_CloseAsync.htm)|
Закрывает соединение с сервисом.  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
[DisposeAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
[DisposeCoreAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_DisposeCoreAsync.htm)|
Вызывается для освобождения ресурсов в дочерних классах.  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync](M_Tessa_Extensions_Default_Console_ManageRoles_Operation_ExecuteAsync.htm)|
Осуществляет выполнение операции.  
(Переопределяет [ConsoleOperation<TContext>.ExecuteAsync(TContext,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_ExecuteAsync.htm))  
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
[LoginAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_LoginAsync.htm)|
Устанавливает соединение с сервисом.  
(Унаследован от
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm))  
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
[Tessa.Extensions.Default.Console.ManageRoles - пространство
имён](N_Tessa_Extensions_Default_Console_ManageRoles.htm)
