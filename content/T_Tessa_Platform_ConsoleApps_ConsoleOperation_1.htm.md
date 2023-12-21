# ConsoleOperation<TContext> \- класс
Базовый класс для операций в консоли.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ConsoleOperation<TContext> : IConsoleOperation<TContext>, 
    	IAsyncDisposable
VB __Копировать
     Public MustInherit Class ConsoleOperation(Of TContext)
    	Implements IConsoleOperation(Of TContext), IAsyncDisposable
C++ __Копировать
    generic<typename TContext>
    public ref class ConsoleOperation abstract : IConsoleOperation<TContext>, 
    	IAsyncDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type ConsoleOperation<'TContext> = 
        class
            interface IConsoleOperation<'TContext>
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleOperation<TContext>
Derived
[Tessa.Extensions.Default.Console.ConvertCards.Operation](T_Tessa_Extensions_Default_Console_ConvertCards_Operation.htm)
[Tessa.Extensions.Default.Console.ConvertConfiguration.Operation](T_Tessa_Extensions_Default_Console_ConvertConfiguration_Operation.htm)
[Tessa.Extensions.Default.Console.CreateFromTemplate.Operation](T_Tessa_Extensions_Default_Console_CreateFromTemplate_Operation.htm)
[Tessa.Extensions.Default.Console.DeleteCards.Operation](T_Tessa_Extensions_Default_Console_DeleteCards_Operation.htm)
[Tessa.Extensions.Default.Console.ExportCards.Operation](T_Tessa_Extensions_Default_Console_ExportCards_Operation.htm)
[Tessa.Extensions.Default.Console.ExportLocalization.Operation](T_Tessa_Extensions_Default_Console_ExportLocalization_Operation.htm)
[Tessa.Extensions.Default.Console.ExportScheme.Operation](T_Tessa_Extensions_Default_Console_ExportScheme_Operation.htm)
[Tessa.Extensions.Default.Console.ExportSearchQueries.Operation](T_Tessa_Extensions_Default_Console_ExportSearchQueries_Operation.htm)
[Tessa.Extensions.Default.Console.ExportTypes.Operation](T_Tessa_Extensions_Default_Console_ExportTypes_Operation.htm)
[Tessa.Extensions.Default.Console.ExportViews.Operation](T_Tessa_Extensions_Default_Console_ExportViews_Operation.htm)
[Tessa.Extensions.Default.Console.ExportWorkplaces.Operation](T_Tessa_Extensions_Default_Console_ExportWorkplaces_Operation.htm)
[Tessa.Extensions.Default.Console.FileSource.Operation](T_Tessa_Extensions_Default_Console_FileSource_Operation.htm)
[Tessa.Extensions.Default.Console.ImportCards.Operation](T_Tessa_Extensions_Default_Console_ImportCards_Operation.htm)
[Tessa.Extensions.Default.Console.ImportLocalization.Operation](T_Tessa_Extensions_Default_Console_ImportLocalization_Operation.htm)
[Tessa.Extensions.Default.Console.ImportScheme.Operation](T_Tessa_Extensions_Default_Console_ImportScheme_Operation.htm)
[Tessa.Extensions.Default.Console.ImportSearchQueries.Operation](T_Tessa_Extensions_Default_Console_ImportSearchQueries_Operation.htm)
[Tessa.Extensions.Default.Console.ImportTypes.Operation](T_Tessa_Extensions_Default_Console_ImportTypes_Operation.htm)
[Tessa.Extensions.Default.Console.ImportUsers.Operation](T_Tessa_Extensions_Default_Console_ImportUsers_Operation.htm)
[Tessa.Extensions.Default.Console.ImportViews.Operation](T_Tessa_Extensions_Default_Console_ImportViews_Operation.htm)
[Tessa.Extensions.Default.Console.ImportWorkplaces.Operation](T_Tessa_Extensions_Default_Console_ImportWorkplaces_Operation.htm)
[Tessa.Extensions.Default.Console.InvalidateCache.Operation](T_Tessa_Extensions_Default_Console_InvalidateCache_Operation.htm)
[Tessa.Extensions.Default.Console.ManageRoles.Operation](T_Tessa_Extensions_Default_Console_ManageRoles_Operation.htm)
[Tessa.Extensions.Default.Console.TimeZone.Operation](T_Tessa_Extensions_Default_Console_TimeZone_Operation.htm)
[Tessa.Extensions.Default.Console.User.Operation](T_Tessa_Extensions_Default_Console_User_Operation.htm)
[Tessa.Platform.ConsoleApps.ClientOperation](T_Tessa_Platform_ConsoleApps_ClientOperation.htm)
[Tessa.Platform.ConsoleApps.ConsoleOperation](T_Tessa_Platform_ConsoleApps_ConsoleOperation.htm)
Подробнее __Less __
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IConsoleOperation](T_Tessa_Platform_ConsoleApps_IConsoleOperation_1.htm)<TContext>
#### Параметры типа
TContext
    Тип контекста операции.
##  __Конструкторы
[ConsoleOperation<TContext>](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[ExtendedInitialization](P_Tessa_Platform_ConsoleApps_ConsoleOperation_1_ExtendedInitialization.htm)|
Признак того, что используется расширенная инициализация при открытии сессии
(с выполняемыми расширениями и стримом инициализации).  
---|---  
[Logger](P_Tessa_Platform_ConsoleApps_ConsoleOperation_1_Logger.htm)|  Логгер
приложения.  
[SessionManager](P_Tessa_Platform_ConsoleApps_ConsoleOperation_1_SessionManager.htm)|
Объект для управления клиентскими сессиями.  
## __Методы
[CheckDisposed](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
---|---  
[CloseAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_CloseAsync.htm)|
Закрывает соединение с сервисом.  
[DisposeAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
[DisposeCoreAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_DisposeCoreAsync.htm)|
Вызывается для освобождения ресурсов в дочерних классах.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync](M_Tessa_Platform_ConsoleApps_ConsoleOperation_1_ExecuteAsync.htm)|
Осуществляет выполнение операции.  
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
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
