# IApplicationModel - интерфейс
Описание интерфейса модели приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationModel : IApplicationMessageObserver, 
    	IDisposable, IComparable, IComparable<IApplicationModel>
VB __Копировать
     Public Interface IApplicationModel
    	Inherits IApplicationMessageObserver, IDisposable, IComparable, IComparable(Of IApplicationModel)
C++ __Копировать
     public interface class IApplicationModel : IApplicationMessageObserver, 
    	IDisposable, IComparable, IComparable<IApplicationModel^>
F# __Копировать
     type IApplicationModel = 
        interface
            interface IApplicationMessageObserver
            interface IDisposable
            interface IComparable
            interface IComparable<IApplicationModel>
        end
Implements
    [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable), [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<IApplicationModel>, [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IApplicationMessageObserver](T_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver.htm)
##  __Свойства
[ApplicationCatalog](P_Tessa_Applications_IApplicationModel_ApplicationCatalog.htm)|
Gets Модель каталога приложений которому принадлежит приложение  
---|---  
[ApplicationPackage](P_Tessa_Applications_IApplicationModel_ApplicationPackage.htm)|
Gets Пакет приложения  
[BaseAddress](P_Tessa_Applications_IApplicationModel_BaseAddress.htm)|  Gets
Базовый адрес сервиса приложения  
[IsDefaultInstance](P_Tessa_Applications_IApplicationModel_IsDefaultInstance.htm)|
Gets or sets a value indicating whether Экземпляр по умолчанию  
[ServerCode](P_Tessa_Applications_IApplicationModel_ServerCode.htm)|  Gets Имя
экземпляра сервиса  
[SkipWinAuth](P_Tessa_Applications_IApplicationModel_SkipWinAuth.htm)|
Признак того, что аутентификация Windows не выполняется, если не введён логин
и пароль.  
[State](P_Tessa_Applications_IApplicationModel_State.htm)|  Gets Состояние
приложения  
## __Методы
[AttachMonitor](M_Tessa_Applications_IApplicationModel_AttachMonitor.htm)|
Устанавливает мониторинг установки приложения  
---|---  
[CompareTo(T)](https://learn.microsoft.com/dotnet/api/system.icomparable-1.compareto#system-
icomparable-1-compareto\(-0\))| Compares the current instance with another
object of the same type and returns an integer that indicates whether the
current instance precedes, follows, or occurs in the same position in the sort
order as the other object.  
(Унаследован от
[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<IApplicationModel>)  
[CompareTo(Object)](https://learn.microsoft.com/dotnet/api/system.icomparable.compareto#system-
icomparable-compareto\(system-object\))| Compares the current instance with
another object of the same type and returns an integer that indicates whether
the current instance precedes, follows, or occurs in the same position in the
sort order as the other object.  
(Унаследован от
[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable))  
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
[LaunchAsync](M_Tessa_Applications_IApplicationModel_LaunchAsync.htm)|
Вызывает запуск приложения  
[OnMessage](M_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver_OnMessage.htm)|
Вызывает обработку сообщения message  
(Унаследован от
[IApplicationMessageObserver](T_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver.htm))  
##  __События
[ApplicationClosed](E_Tessa_Applications_IApplicationModel_ApplicationClosed.htm)|
Событие закрытия приложения  
---|---  
[ApplicationLaunched](E_Tessa_Applications_IApplicationModel_ApplicationLaunched.htm)|
Событие успешного запуска приложения  
[ApplicationLaunchFailed](E_Tessa_Applications_IApplicationModel_ApplicationLaunchFailed.htm)|
Событие сбоя при запуске приложения  
## __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
