# IApplicationCatalog - интерфейс
Описание интерфейса каталога приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationCatalog : IStorageElementSerialization, 
    	IComparable, INotifyPropertyChanged
VB __Копировать
     Public Interface IApplicationCatalog
    	Inherits IStorageElementSerialization, IComparable, INotifyPropertyChanged
C++ __Копировать
     public interface class IApplicationCatalog : IStorageElementSerialization, 
    	IComparable, INotifyPropertyChanged
F# __Копировать
     type IApplicationCatalog = 
        interface
            interface IStorageElementSerialization
            interface IComparable
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable), [IStorageElementSerialization](T_Tessa_Applications_Containers_Storage_IStorageElementSerialization.htm)
##  __Свойства
[Alias](P_Tessa_Applications_IApplicationCatalog_Alias.htm)|  Gets Название
каталога  
---|---  
[IsDefault](P_Tessa_Applications_IApplicationCatalog_IsDefault.htm)|  Gets a
value indicating whether Признак каталога по умолчанию  
[LaunchedApplicationsCount](P_Tessa_Applications_IApplicationCatalog_LaunchedApplicationsCount.htm)|
Gets Возвращает количество приложений из каталога находящихся в состоянии
попытки запуска или запущенном состоянии  
[LoadingState](P_Tessa_Applications_IApplicationCatalog_LoadingState.htm)|
Gets or sets Устанавливает состояние загрузки приложений  
[OpenTimeOut](P_Tessa_Applications_IApplicationCatalog_OpenTimeOut.htm)|  Gets
Тайм-аут ожидания подключения к сервису  
[Parent](P_Tessa_Applications_IApplicationCatalog_Parent.htm)|  Gets or sets
Владелец каталогов приложений  
[Password](P_Tessa_Applications_IApplicationCatalog_Password.htm)|  Gets
Пароль  
[Path](P_Tessa_Applications_IApplicationCatalog_Path.htm)|  Gets Путь к
каталогу приложений  
[SkipWinAuth](P_Tessa_Applications_IApplicationCatalog_SkipWinAuth.htm)|
Признак того, что аутентификация Windows не выполняется, если не введён логин
и пароль.  
[UserName](P_Tessa_Applications_IApplicationCatalog_UserName.htm)|  Gets Имя
пользователя  
## __Методы
[CompareTo](https://learn.microsoft.com/dotnet/api/system.icomparable.compareto#system-
icomparable-compareto\(system-object\))| Compares the current instance with
another object of the same type and returns an integer that indicates whether
the current instance precedes, follows, or occurs in the same position in the
sort order as the other object.  
(Унаследован от
[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable))  
---|---  
[DecLaunchedApplicationsCount](M_Tessa_Applications_IApplicationCatalog_DecLaunchedApplicationsCount.htm)|
Уменьшает число запущенных приложений  
[IncLaunchedApplicationsCount](M_Tessa_Applications_IApplicationCatalog_IncLaunchedApplicationsCount.htm)|
Увеличивает число запущенных приложений  
[Serialize](M_Tessa_Applications_Containers_Storage_IStorageElementSerialization_Serialize.htm)|
Осущестляет запись свойств объекта в элемент container  
(Унаследован от
[IStorageElementSerialization](T_Tessa_Applications_Containers_Storage_IStorageElementSerialization.htm))  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
