# ISettings - интерфейс
Настройки расширений.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISettings : ISealable
VB __Копировать
     Public Interface ISettings
    	Inherits ISealable
C++ __Копировать
     public interface class ISettings : ISealable
F# __Копировать
     type ISettings = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[Info](P_Tessa_Platform_Settings_ISettings_Info.htm)|  Дополнительные
настройки расширений, представленные в неструктурируемом виде. Укажите любые
настройки своего модуля или проектного решения здесь.  
---|---  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[MaxCardTypeTilesBeforeAddingSubgroup](P_Tessa_Platform_Settings_ISettings_MaxCardTypeTilesBeforeAddingSubgroup.htm)|
Максимальное количество доступных плиток на создание карточек, которые могут
отображаться внутри группы с типами карточек. По умолчанию 12.  
[MaxCardTypeTilesWithoutGrouping](P_Tessa_Platform_Settings_ISettings_MaxCardTypeTilesWithoutGrouping.htm)|
Максимальное количество доступных плиток на создание карточек, которые могут
отображаться без группировки плоским списком. По умолчанию 12.  
[MaxDocTypeTilesWithoutGroupingByCardType](P_Tessa_Platform_Settings_ISettings_MaxDocTypeTilesWithoutGroupingByCardType.htm)|
Максимальное количество доступных типов документов до того, как они будут
сгруппированы по типам карточек. По умолчанию 12.  
[MaxFileContentNameLength](P_Tessa_Platform_Settings_ISettings_MaxFileContentNameLength.htm)|
Максимальная длина имени файла с расширением, но без пути к файлу, в кэше
файлов (во временной папке). Используется в desktop-клиенте при определении в
клиентских расширениях. Значение должно быть неотрицательным числом. Укажите
0, если ограничение отсутствует. По умолчанию равно 100.  
[MaxSettingsTilesBeforeAddingSubgroup](P_Tessa_Platform_Settings_ISettings_MaxSettingsTilesBeforeAddingSubgroup.htm)|
Максимальное количество доступных плиток на открытие карточек настроек,
которые могут отображаться до того, как будет добавлена плитка "ещё". По
умолчанию 12.  
[MaxViewFilterTextInCardLength](P_Tessa_Platform_Settings_ISettings_MaxViewFilterTextInCardLength.htm)|
Максимальная длина текста в фильтре контрола представления в карточке до его
сворачивания. Используется в desktop-клиенте при определении в клиентских
расширениях. Значение должно быть неотрицательным числом. Укажите 0, если
ограничение отсутствует. По умолчанию равно 150.  
[MaxViewFilterTextInWorkplaceLength](P_Tessa_Platform_Settings_ISettings_MaxViewFilterTextInWorkplaceLength.htm)|
Максимальная длина текста в фильтре контрола представления на рабочем месте до
его сворачивания. Используется в desktop-клиенте при определении в клиентских
расширениях. Значение должно быть неотрицательным числом. Укажите 0, если
ограничение отсутствует. По умолчанию равно 150.  
[MaxWallpaperTilesBeforeAddingSubgroup](P_Tessa_Platform_Settings_ISettings_MaxWallpaperTilesBeforeAddingSubgroup.htm)|
Максимальное количество доступных плиток на изменение фона, которые
отображаются до появления плитки "ещё" с разбиением списка плиток на несколько
страниц. По умолчанию 12.  
[MinActionsGroupingCount](P_Tessa_Platform_Settings_ISettings_MinActionsGroupingCount.htm)|
Минимальное количество одновременно доступных пользователю плиток, которые
будут сгруппированы в группу "Действия". По умолчанию количество равно 2.
Значение должно быть положительным числом.  
[UserLimitToShowForDynamicAndMetaRoles](P_Tessa_Platform_Settings_ISettings_UserLimitToShowForDynamicAndMetaRoles.htm)|
Максимальное количество пользователей, отображаемых в составе динамических и
метаролей. Может быть указано отрицательное число, если количество
пользователей не ограничено. По умолчанию 200. Количество пользователей
ограничивается только при стандартном запросе с клиента. Когда выполняется
запрос на загрузку ролей на сервере (в т.ч. в плагинах Chronos) или
выполняется специальный запрос (такой как экспорт или просмотр структуры), то
состав роли не ограничивается независимо от настройки.  
[UserSettingsCardTypeIDList](P_Tessa_Platform_Settings_ISettings_UserSettingsCardTypeIDList.htm)|
Список идентификаторов типов карточек, которые расширяют "Мои настройки" для
настроек сотрудников. Порядок в списке определяет порядок отображения настроек
в UI.  
## __Методы
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
[Set](M_Tessa_Platform_Settings_ISettings_Set.htm)|  Задаёт
строготипизированный объект с настройками, который будет в дальнейшем доступен
по типу объекта. Если объект этого типа уже был задан, то новый объект его
перезапишет.  
[TryGet](M_Tessa_Platform_Settings_ISettings_TryGet.htm)|  Получает
строготипизированный объект с настройками заданного типа или null, если объект
не был добавлен.  
## __Методы расширения
[Get<T>](M_Tessa_Platform_Settings_SettingsExtensions_Get__1.htm)|  Получает
объект с настройками заданного типа. Результирующий объект гарантированно не
равен null. Если объект не зарегистрирован, то выбрасывает
[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception).  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
---|---  
[TryGet<T>](M_Tessa_Platform_Settings_SettingsExtensions_TryGet__1.htm)|
Получает объект с настройками заданного типа или null, если объект не
зарегистрирован.  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
