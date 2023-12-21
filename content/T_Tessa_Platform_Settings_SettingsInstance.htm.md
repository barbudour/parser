# SettingsInstance - класс
Настройки расширений.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SettingsInstance : ISettings, 
    	ISealable
VB __Копировать
     Public Class SettingsInstance
    	Implements ISettings, ISealable
C++ __Копировать
     public ref class SettingsInstance : ISettings, 
    	ISealable
F# __Копировать
     type SettingsInstance = 
        class
            interface ISettings
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SettingsInstance
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [ISettings](T_Tessa_Platform_Settings_ISettings.htm)
##  __Заметки
Наследники класса могут добавлять свойства и переопределять метод
[SealInternal()](M_Tessa_Platform_Settings_SettingsInstance_SealInternal.htm).
## __Конструкторы
[SettingsInstance](M_Tessa_Platform_Settings_SettingsInstance__ctor.htm)|
Инициализирует новый экземпляр класса SettingsInstance  
---|---  
##  __Свойства
[Info](P_Tessa_Platform_Settings_SettingsInstance_Info.htm)|  Дополнительные
настройки расширений, представленные в неструктурируемом виде. Укажите любые
настройки своего модуля или проектного решения здесь.  
---|---  
[IsSealed](P_Tessa_Platform_Settings_SettingsInstance_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[MaxCardTypeTilesBeforeAddingSubgroup](P_Tessa_Platform_Settings_SettingsInstance_MaxCardTypeTilesBeforeAddingSubgroup.htm)|
Максимальное количество доступных плиток на создание карточек, которые могут
отображаться внутри группы с типами карточек. По умолчанию 12.  
[MaxCardTypeTilesWithoutGrouping](P_Tessa_Platform_Settings_SettingsInstance_MaxCardTypeTilesWithoutGrouping.htm)|
Максимальное количество доступных плиток на создание карточек, которые могут
отображаться без группировки плоским списком. По умолчанию 12.  
[MaxDocTypeTilesWithoutGroupingByCardType](P_Tessa_Platform_Settings_SettingsInstance_MaxDocTypeTilesWithoutGroupingByCardType.htm)|
Максимальное количество доступных типов документов до того, как они будут
сгруппированы по типам карточек. По умолчанию 12.  
[MaxFileContentNameLength](P_Tessa_Platform_Settings_SettingsInstance_MaxFileContentNameLength.htm)|
Максимальная длина имени файла с расширением, но без пути к файлу, в кэше
файлов (во временной папке). Используется в desktop-клиенте при определении в
клиентских расширениях. Значение должно быть неотрицательным числом. Укажите
0, если ограничение отсутствует. По умолчанию равно 100.  
[MaxSettingsTilesBeforeAddingSubgroup](P_Tessa_Platform_Settings_SettingsInstance_MaxSettingsTilesBeforeAddingSubgroup.htm)|
Максимальное количество доступных плиток на открытие карточек настроек,
которые могут отображаться до того, как будет добавлена плитка "ещё". По
умолчанию 12.  
[MaxViewFilterTextInCardLength](P_Tessa_Platform_Settings_SettingsInstance_MaxViewFilterTextInCardLength.htm)|
Максимальная длина текста в фильтре контрола представления в карточке до его
сворачивания. Используется в desktop-клиенте при определении в клиентских
расширениях. Значение должно быть неотрицательным числом. Укажите 0, если
ограничение отсутствует. По умолчанию равно 150.  
[MaxViewFilterTextInWorkplaceLength](P_Tessa_Platform_Settings_SettingsInstance_MaxViewFilterTextInWorkplaceLength.htm)|
Максимальная длина текста в фильтре контрола представления на рабочем месте до
его сворачивания. Используется в desktop-клиенте при определении в клиентских
расширениях. Значение должно быть неотрицательным числом. Укажите 0, если
ограничение отсутствует. По умолчанию равно 150.  
[MaxWallpaperTilesBeforeAddingSubgroup](P_Tessa_Platform_Settings_SettingsInstance_MaxWallpaperTilesBeforeAddingSubgroup.htm)|
Максимальное количество доступных плиток на изменение фона, которые
отображаются до появления плитки "ещё" с разбиением списка плиток на несколько
страниц. По умолчанию 12.  
[MinActionsGroupingCount](P_Tessa_Platform_Settings_SettingsInstance_MinActionsGroupingCount.htm)|
Минимальное количество одновременно доступных пользователю плиток, которые
будут сгруппированы в группу "Действия". По умолчанию количество равно 2.
Значение должно быть положительным числом.  
[UserLimitToShowForDynamicAndMetaRoles](P_Tessa_Platform_Settings_SettingsInstance_UserLimitToShowForDynamicAndMetaRoles.htm)|
Максимальное количество пользователей, отображаемых в составе динамических и
метаролей. Может быть указано отрицательное число, если количество
пользователей не ограничено. По умолчанию 200. Количество пользователей
ограничивается только при стандартном запросе с клиента. Когда выполняется
запрос на загрузку ролей на сервере (в т.ч. в плагинах Chronos) или
выполняется специальный запрос (такой как экспорт или просмотр структуры), то
состав роли не ограничивается независимо от настройки.  
[UserSettingsCardTypeIDList](P_Tessa_Platform_Settings_SettingsInstance_UserSettingsCardTypeIDList.htm)|
Список идентификаторов типов карточек, которые расширяют "Мои настройки" для
настроек сотрудников. Порядок в списке определяет порядок отображения настроек
в UI.  
## __Методы
[CheckSealed](M_Tessa_Platform_Settings_SettingsInstance_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
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
[Seal](M_Tessa_Platform_Settings_SettingsInstance_Seal.htm)| Защищает объект
от изменений.  
[SealInternal](M_Tessa_Platform_Settings_SettingsInstance_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[Set](M_Tessa_Platform_Settings_SettingsInstance_Set.htm)|  Задаёт
строготипизированный объект с настройками, который будет в дальнейшем доступен
по типу объекта. Если объект этого типа уже был задан, то новый объект его
перезапишет.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Settings_SettingsInstance_TryGet.htm)|  Получает
строготипизированный объект с настройками заданного типа или null, если объект
не был добавлен.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[Get<T>](M_Tessa_Platform_Settings_SettingsExtensions_Get__1.htm)|  Получает
объект с настройками заданного типа. Результирующий объект гарантированно не
равен null. Если объект не зарегистрирован, то выбрасывает
[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception).  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
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
[TryGet<T>](M_Tessa_Platform_Settings_SettingsExtensions_TryGet__1.htm)|
Получает объект с настройками заданного типа или null, если объект не
зарегистрирован.  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
