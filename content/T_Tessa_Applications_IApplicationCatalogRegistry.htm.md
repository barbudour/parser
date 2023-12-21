# IApplicationCatalogRegistry - интерфейс
Описание интерфейса сервиса каталогов приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationCatalogRegistry : IStorageElementSerialization, 
    	INotifyPropertyChanged
VB __Копировать
     Public Interface IApplicationCatalogRegistry
    	Inherits IStorageElementSerialization, INotifyPropertyChanged
C++ __Копировать
     public interface class IApplicationCatalogRegistry : IStorageElementSerialization, 
    	INotifyPropertyChanged
F# __Копировать
     type IApplicationCatalogRegistry = 
        interface
            interface IStorageElementSerialization
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IStorageElementSerialization](T_Tessa_Applications_Containers_Storage_IStorageElementSerialization.htm)
##  __Свойства
[Catalogs](P_Tessa_Applications_IApplicationCatalogRegistry_Catalogs.htm)|
Gets Возвращает список компонентов контейнера расположенных непосредственно в
самом контейнере.  
---|---  
[DefaultCatalog](P_Tessa_Applications_IApplicationCatalogRegistry_DefaultCatalog.htm)|
Gets or sets Каталог по умолчанию.  
[DisableAppManagerUpdates](P_Tessa_Applications_IApplicationCatalogRegistry_DisableAppManagerUpdates.htm)|
Признак того, что обновления ApplicationManager из каталога
[DefaultCatalog](P_Tessa_Applications_IApplicationCatalogRegistry_DefaultCatalog.htm)
отключены.  
## __Методы
[Add](M_Tessa_Applications_IApplicationCatalogRegistry_Add.htm)|  Добавляет
компонент catalog в контейнер. Добавляемый компонент должен быть не равен
null.  
---|---  
[Clear](M_Tessa_Applications_IApplicationCatalogRegistry_Clear.htm)|
Осуществляет удаление из контейнера всех элементов  
[Remove](M_Tessa_Applications_IApplicationCatalogRegistry_Remove.htm)|
Удаляет компонент catalog из контейнера. Удаляемый компонент должен быть не
равен null  
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
##  __Методы расширения
[TryGetItem](M_Tessa_UI_AppManager_CatalogService_ApplicationCatalogServiceExtender_TryGetItem.htm)|
Получает и возвращает информацию о каталоге приложений с именем name. Если
каталог с таким именем отсутствует возвращает null  
(Определяется
[ApplicationCatalogServiceExtender](T_Tessa_UI_AppManager_CatalogService_ApplicationCatalogServiceExtender.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
