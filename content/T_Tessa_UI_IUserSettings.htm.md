# IUserSettings - интерфейс
Настройки, применяемые для клиентского рабочего места.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUserSettings
VB __Копировать
     Public Interface IUserSettings
C++ __Копировать
     public interface class IUserSettings
F# __Копировать
     type IUserSettings = interface end
##  __Свойства
[AllowMultipleExternalPreview](P_Tessa_UI_IUserSettings_AllowMultipleExternalPreview.htm)|
Признак того, что требуется разрешить предпросмотр одновременно через
несколько внешних программ (на разных вкладках). Если указано false (по
умолчанию), то при активации предпросмотра через внешнюю программу на одной
вкладке очищается область предпросмотра через внешнюю программу в другой
вкладке.  
---|---  
[CustomBackgroundColors](P_Tessa_UI_IUserSettings_CustomBackgroundColors.htm)|
Набор пользовательских цветов для цвета фона текста.  
[CustomBlockColors](P_Tessa_UI_IUserSettings_CustomBlockColors.htm)| Набор
пользовательских цветов для цвета фона блока.  
[CustomForegroundColors](P_Tessa_UI_IUserSettings_CustomForegroundColors.htm)|
Набор пользовательских цветов для цвета текста.  
[Data](P_Tessa_UI_IUserSettings_Data.htm)| Данные по настройкам сотрудника.
Настройки могут быть добавлены в типовом и в проектном решении.  
[DisablePdfEmbeddedPreview](P_Tessa_UI_IUserSettings_DisablePdfEmbeddedPreview.htm)|
Признак того, что требуется отключить встроенный предпросмотр PDF и
использовать внешнюю программу.  
[DisablePopupNotifications](P_Tessa_UI_IUserSettings_DisablePopupNotifications.htm)|
Признак того, что всплывающие уведомления в приложениях будут отключены.  
[DisableWindowFading](P_Tessa_UI_IUserSettings_DisableWindowFading.htm)|
Признак того, что запрещено затемнение экрана, когда окно не в фокусе.  
[DoNotShowMessageIndicatorOnStartup](P_Tessa_UI_IUserSettings_DoNotShowMessageIndicatorOnStartup.htm)|
Признак того, что необходимо не показывать индикатор сообщений при запуске.  
[EnableMessageIndicator](P_Tessa_UI_IUserSettings_EnableMessageIndicator.htm)|
Признак того, что индикатор сообщений отображается.  
[ForumsRefreshInterval](P_Tessa_UI_IUserSettings_ForumsRefreshInterval.htm)|
Периода обновления форумов на клиенте в секундах.  
[LeftPanelBottomAreaOpenOnClick](P_Tessa_UI_IUserSettings_LeftPanelBottomAreaOpenOnClick.htm)|
Признак того, что левая боковая панель открывается не при наведении мыши на
левый нижний угол экрана, а при клике по этой области.  
[LeftPanelOpenOnClick](P_Tessa_UI_IUserSettings_LeftPanelOpenOnClick.htm)|
Признак того, что левая боковая панель открывается не при наведении мыши на
полосу слева, а при клике по этой полосе.  
[LeftPanelTopAreaOpenOnClick](P_Tessa_UI_IUserSettings_LeftPanelTopAreaOpenOnClick.htm)|
Признак того, что левая боковая панель открывается не при наведении мыши на
левый верхний угол экрана, а при клике по этой области.  
[PreferPdfPagingPreview](P_Tessa_UI_IUserSettings_PreferPdfPagingPreview.htm)|
Признак того, что для встроенного предпросмотра PDF предпочитается
использование постраничного просмотра. Значение по умолчанию false
соответствует режиму сквозной прокрутки между страницами.  
[RightPanelBottomAreaOpenOnClick](P_Tessa_UI_IUserSettings_RightPanelBottomAreaOpenOnClick.htm)|
Признак того, что правая боковая панель открывается не при наведении мыши на
правый нижний угол экрана, а при клике по этой области.  
[RightPanelOpenOnClick](P_Tessa_UI_IUserSettings_RightPanelOpenOnClick.htm)|
Признак того, что правая боковая панель открывается не при наведении мыши на
полосу справа, а при клике по этой полосе.  
[RightPanelTopAreaOpenOnClick](P_Tessa_UI_IUserSettings_RightPanelTopAreaOpenOnClick.htm)|
Признак того, что правая боковая панель открывается не при наведении мыши на
правый верхний угол экрана, а при клике по этой области.  
[TaskColor](P_Tessa_UI_IUserSettings_TaskColor.htm)| Цвет заданий по
умолчанию.  
[TaskColorsByFunctionRoleID](P_Tessa_UI_IUserSettings_TaskColorsByFunctionRoleID.htm)|
Цвет для заданий, которые пользователь видит при непосредственном вхождении в
функциональную роль или при вхождении в неё как заместитель. Цвета доступны по
идентификатору функциональной роли.  
[TopicItemColor](P_Tessa_UI_IUserSettings_TopicItemColor.htm)| Цвет обсуждений
в области с заданиями по умолчанию.  
##  __Методы
[NotifyModified](M_Tessa_UI_IUserSettings_NotifyModified.htm)|  Уведомляет
подписчиков события [Tessa.UI.Tiles.IUserSettings.Modified] о том, что одно
или несколько свойств объекта были изменены.  
---|---  
[Set](M_Tessa_UI_IUserSettings_Set.htm)| Устанавливает свойства текущего
объекта по свойствам заданного объекта.  
[UpdatePropertiesFromDataAsync](M_Tessa_UI_IUserSettings_UpdatePropertiesFromDataAsync.htm)|
Устанавливает свойства текущего объекта по данным, установленным в свойстве
[Tessa.UI.IUserSettings.Data].  
## __События
[Modified](E_Tessa_UI_IUserSettings_Modified.htm)| Событие, уведомляющее об
изменениях свойств текущего объекта с настройками.  
---|---  
##  __Методы расширения
[Get<T>](M_Tessa_UI_UIExtensions_Get__1.htm)|  Возвращает значение поля в
строковой секции, заданной в пользовательских настройках. Если секция или поле
не найдены, то выбрасывается
[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception).  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
[GetSection](M_Tessa_UI_UIExtensions_GetSection.htm)|  Возвращает секцию,
заданную в пользовательских настройках.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[GetTaskColors](M_Tessa_UI_UIExtensions_GetTaskColors.htm)|  Возвращает цвета
заданий, задействуемые для функциональной роли с идентификатором
functionRoleID в соответствии с настройками пользователя. Если в настройках
отсутствует информация по роли, то возвращается объект, содержащий все
свойства как null.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[SetupFromJsonAsync](M_Tessa_UI_UIExtensions_SetupFromJsonAsync.htm)|
Устанавливает настройки в соответствии с сериализованными в текстовый JSON
значениями.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[TryGet<T>](M_Tessa_UI_UIExtensions_TryGet__1.htm)|  Возвращает значение поля
в строковой секции, заданной в пользовательских настройках, или значение по
умолчанию defaultValue, если секция или поле не найдены.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[TryGetFields<TFrom, TTo>](M_Tessa_UI_UIExtensions_TryGetFields__2.htm)|
Возвращает список значений указанной секции  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[TryGetSection](M_Tessa_UI_UIExtensions_TryGetSection.htm)|  Возвращает
секцию, заданную в пользовательских настройках, или null, если секцию не
удалось получить.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
