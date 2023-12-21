# TessaApplication - класс
Приложение WPF, использующее сессию Tessa.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class TessaApplication : Application
VB __Копировать
     Public MustInherit Class TessaApplication
    	Inherits Application
C++ __Копировать
     public ref class TessaApplication abstract : public Application
F# __Копировать
     [<AbstractClassAttribute>]
    type TessaApplication = 
        class
            inherit Application
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject) __[Application](https://learn.microsoft.com/dotnet/api/system.windows.application) __ TessaApplication
##  __Конструкторы
[TessaApplication](M_Tessa_UI_TessaApplication__ctor.htm)| Инициализирует
новый экземпляр класса TessaApplication  
---|---  
##  __Свойства
[Application](P_Tessa_UI_TessaApplication_Application.htm)|  Текущее
запущенное приложение или null, если приложение ещё не было запущено или было
завершено.  
---|---  
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.dispatcher#system-
windows-threading-dispatcherobject-dispatcher)| Gets the
[Dispatcher](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcher)
this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject)
is associated with.  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[IsLaunched](P_Tessa_UI_TessaApplication_IsLaunched.htm)|  Признак того, что
приложение было успешно запущено.  
[LauncherSplash](P_Tessa_UI_TessaApplication_LauncherSplash.htm)|  Содержит
отображаемое при загрузке приложения окно  
[MainWindow](https://learn.microsoft.com/dotnet/api/system.windows.application.mainwindow#system-
windows-application-mainwindow)| Gets or sets the main window of the
application.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Properties](https://learn.microsoft.com/dotnet/api/system.windows.application.properties#system-
windows-application-properties)| Gets a collection of application-scope
properties.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[PublishModeByDefault](P_Tessa_UI_TessaApplication_PublishModeByDefault.htm)|
Признак того, что приложение по умолчанию запускается всегда в режиме
публикации, даже без параметра /publish. Требуется для того, чтобы определить,
выполняет ли приложение публикацию в "тихом" режиме.  
[Resources](https://learn.microsoft.com/dotnet/api/system.windows.application.resources#system-
windows-application-resources)| Gets or sets a collection of application-scope
resources, such as styles and brushes.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[ShutdownMode](https://learn.microsoft.com/dotnet/api/system.windows.application.shutdownmode#system-
windows-application-shutdownmode)| Gets or sets the condition that causes the
[Shutdown()](https://learn.microsoft.com/dotnet/api/system.windows.application.shutdown#system-
windows-application-shutdown) method to be called.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[StartupUri](https://learn.microsoft.com/dotnet/api/system.windows.application.startupuri#system-
windows-application-startupuri)| Gets or sets a UI that is automatically shown
when an application starts.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[ThemeWindowTypes](P_Tessa_UI_TessaApplication_ThemeWindowTypes.htm)|
Нестандартные типы окон, не являющиеся наследниками
[TessaWindow](T_Tessa_UI_Windows_TessaWindow.htm). Значение может быть равно
null, если такие типы отсутствуют. Изменять значение свойства необходимо перед
вызовом метода
[OnStartup(StartupEventArgs)](M_Tessa_UI_TessaApplication_OnStartup.htm),
например, в конструкторе.  
[UnityContainer](P_Tessa_UI_TessaApplication_UnityContainer.htm)|  Текущий
используемый контейнер Unity или null, если приложение ещё не было запущено,
было завершено или не связано с контейнером.  
[Windows](https://learn.microsoft.com/dotnet/api/system.windows.application.windows#system-
windows-application-windows)| Gets the instantiated windows in an application.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
##  __Методы
[ActivateShell](M_Tessa_UI_TessaApplication_ActivateShell.htm)|  Активирует
главное окно по умолчанию. Стандартной реализации, которая активирует окно
[MainWindow](https://learn.microsoft.com/dotnet/api/system.windows.application.mainwindow#system-
windows-application-mainwindow), достаточно для обычных окон.  
---|---  
[CheckAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.checkaccess#system-
windows-threading-dispatcherobject-checkaccess)| Determines whether the
calling thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
[FindResource](https://learn.microsoft.com/dotnet/api/system.windows.application.findresource#system-
windows-application-findresource\(system-object\))| Searches for a user
interface (UI) resource, such as a
[Style](https://learn.microsoft.com/dotnet/api/system.windows.style) or
[Brush](https://learn.microsoft.com/dotnet/api/system.windows.media.brush),
with the specified key, and throws an exception if the requested resource is
not found (see XAML Resources).  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnActivated](https://learn.microsoft.com/dotnet/api/system.windows.application.onactivated#system-
windows-application-onactivated\(system-eventargs\))| Raises the
[Activated](https://learn.microsoft.com/dotnet/api/system.windows.application.activated)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnApplicationExitAsync](M_Tessa_UI_TessaApplication_OnApplicationExitAsync.htm)|
Переопределите метод для того, чтобы выполнить дополнительные действия по
завершению работы приложения. Если специальных действий выполнять не
требуется, то переопределять метод не рекомендуется.  
[OnApplicationStartupAsync](M_Tessa_UI_TessaApplication_OnApplicationStartupAsync.htm)|
Переопределите метод для того, чтобы запустить приложение и установить
свойства [Application](P_Tessa_UI_TessaApplication_Application.htm) и
[UnityContainer](P_Tessa_UI_TessaApplication_UnityContainer.htm).  
[OnDeactivated](https://learn.microsoft.com/dotnet/api/system.windows.application.ondeactivated#system-
windows-application-ondeactivated\(system-eventargs\))| Raises the
[Deactivated](https://learn.microsoft.com/dotnet/api/system.windows.application.deactivated)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnExit](M_Tessa_UI_TessaApplication_OnExit.htm)|  Стандартный обработчик
завершения приложения.  
(Переопределяет
[Application.OnExit(ExitEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.application.onexit#system-
windows-application-onexit\(system-windows-exiteventargs\)))  
[OnFragmentNavigation](https://learn.microsoft.com/dotnet/api/system.windows.application.onfragmentnavigation#system-
windows-application-onfragmentnavigation\(system-windows-navigation-
fragmentnavigationeventargs\))| Raises the
[FragmentNavigation](https://learn.microsoft.com/dotnet/api/system.windows.application.fragmentnavigation)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnLoadCompleted](https://learn.microsoft.com/dotnet/api/system.windows.application.onloadcompleted#system-
windows-application-onloadcompleted\(system-windows-navigation-
navigationeventargs\))| Raises the
[LoadCompleted](https://learn.microsoft.com/dotnet/api/system.windows.application.loadcompleted)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnNavigated](https://learn.microsoft.com/dotnet/api/system.windows.application.onnavigated#system-
windows-application-onnavigated\(system-windows-navigation-
navigationeventargs\))| Raises the
[Navigated](https://learn.microsoft.com/dotnet/api/system.windows.application.navigated)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnNavigating](https://learn.microsoft.com/dotnet/api/system.windows.application.onnavigating#system-
windows-application-onnavigating\(system-windows-navigation-
navigatingcanceleventargs\))| Raises the
[Navigating](https://learn.microsoft.com/dotnet/api/system.windows.application.navigating)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnNavigationFailed](https://learn.microsoft.com/dotnet/api/system.windows.application.onnavigationfailed#system-
windows-application-onnavigationfailed\(system-windows-navigation-
navigationfailedeventargs\))| Raises the
[NavigationFailed](https://learn.microsoft.com/dotnet/api/system.windows.application.navigationfailed)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnNavigationProgress](https://learn.microsoft.com/dotnet/api/system.windows.application.onnavigationprogress#system-
windows-application-onnavigationprogress\(system-windows-navigation-
navigationprogresseventargs\))| Raises the
[NavigationProgress](https://learn.microsoft.com/dotnet/api/system.windows.application.navigationprogress)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnNavigationStopped](https://learn.microsoft.com/dotnet/api/system.windows.application.onnavigationstopped#system-
windows-application-onnavigationstopped\(system-windows-navigation-
navigationeventargs\))| Raises the
[NavigationStopped](https://learn.microsoft.com/dotnet/api/system.windows.application.navigationstopped)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnSessionEnding](https://learn.microsoft.com/dotnet/api/system.windows.application.onsessionending#system-
windows-application-onsessionending\(system-windows-
sessionendingcanceleventargs\))| Raises the
[SessionEnding](https://learn.microsoft.com/dotnet/api/system.windows.application.sessionending)
event.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[OnStartup](M_Tessa_UI_TessaApplication_OnStartup.htm)|  Стандартный
обработчик запуска приложения.  
(Переопределяет
[Application.OnStartup(StartupEventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.application.onstartup#system-
windows-application-onstartup\(system-windows-startupeventargs\)))  
[Run()](https://learn.microsoft.com/dotnet/api/system.windows.application.run#system-
windows-application-run)| Starts a Windows Presentation Foundation
application.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Run(Window)](https://learn.microsoft.com/dotnet/api/system.windows.application.run#system-
windows-application-run\(system-windows-window\))| Starts a Windows
Presentation Foundation application and opens the specified window.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Shutdown()](https://learn.microsoft.com/dotnet/api/system.windows.application.shutdown#system-
windows-application-shutdown)| Shuts down an application.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Shutdown(Int32)](https://learn.microsoft.com/dotnet/api/system.windows.application.shutdown#system-
windows-application-shutdown\(system-int32\))| Shuts down an application that
returns the specified exit code to the operating system.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[TryCreateLauncherSplash](M_Tessa_UI_TessaApplication_TryCreateLauncherSplash.htm)|
Метод, создающий сплэш, отображаемый при запуске и инициализации приложения,
или null, если сплэш не должен отображаться.  
[TryFindResource](https://learn.microsoft.com/dotnet/api/system.windows.application.tryfindresource#system-
windows-application-tryfindresource\(system-object\))| Searches for the
specified resource.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[VerifyAccess](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject.verifyaccess#system-
windows-threading-dispatcherobject-verifyaccess)| Enforces that the calling
thread has access to this
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject).  
(Унаследован от
[DispatcherObject](https://learn.microsoft.com/dotnet/api/system.windows.threading.dispatcherobject))  
##  __События
[Activated](https://learn.microsoft.com/dotnet/api/system.windows.application.activated)|
Occurs when an application becomes the foreground application.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
---|---  
[Deactivated](https://learn.microsoft.com/dotnet/api/system.windows.application.deactivated)|
Occurs when an application stops being the foreground application.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[DispatcherUnhandledException](https://learn.microsoft.com/dotnet/api/system.windows.application.dispatcherunhandledexception)|
Occurs when an exception is thrown by an application but not handled.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Exit](https://learn.microsoft.com/dotnet/api/system.windows.application.exit)|
Occurs just before an application shuts down and cannot be canceled.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[FragmentNavigation](https://learn.microsoft.com/dotnet/api/system.windows.application.fragmentnavigation)|
Occurs when a navigator in the application begins navigation to a content
fragment, Navigation occurs immediately if the desired fragment is in the
current content, or after the source XAML content has been loaded if the
desired fragment is in different content.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[LoadCompleted](https://learn.microsoft.com/dotnet/api/system.windows.application.loadcompleted)|
Occurs when content that was navigated to by a navigator in the application
has been loaded, parsed, and has begun rendering.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Navigated](https://learn.microsoft.com/dotnet/api/system.windows.application.navigated)|
Occurs when the content that is being navigated to by a navigator in the
application has been found, although it may not have completed loading.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Navigating](https://learn.microsoft.com/dotnet/api/system.windows.application.navigating)|
Occurs when a new navigation is requested by a navigator in the application.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[NavigationFailed](https://learn.microsoft.com/dotnet/api/system.windows.application.navigationfailed)|
Occurs when an error occurs while a navigator in the application is navigating
to the requested content.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[NavigationProgress](https://learn.microsoft.com/dotnet/api/system.windows.application.navigationprogress)|
Occurs periodically during a download that is being managed by a navigator in
the application to provide navigation progress information.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[NavigationStopped](https://learn.microsoft.com/dotnet/api/system.windows.application.navigationstopped)|
Occurs when the StopLoading method of a navigator in the application is
called, or when a new navigation is requested by a navigator while a current
navigation is in progress.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[SessionEnding](https://learn.microsoft.com/dotnet/api/system.windows.application.sessionending)|
Occurs when the user ends the Windows session by logging off or shutting down
the operating system.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
[Startup](https://learn.microsoft.com/dotnet/api/system.windows.application.startup)|
Occurs when the
[Run()](https://learn.microsoft.com/dotnet/api/system.windows.application.run#system-
windows-application-run) method of the
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application)
object is called.  
(Унаследован от
[Application](https://learn.microsoft.com/dotnet/api/system.windows.application))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
