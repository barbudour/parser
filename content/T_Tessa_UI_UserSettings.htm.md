# UserSettings - класс
Настройки, применяемые для клиентского рабочего места.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UserSettings : IUserSettings
VB __Копировать
     Public NotInheritable Class UserSettings
    	Implements IUserSettings
C++ __Копировать
     public ref class UserSettings sealed : IUserSettings
F# __Копировать
     [<SealedAttribute>]
    type UserSettings = 
        class
            interface IUserSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UserSettings
Implements
    [IUserSettings](T_Tessa_UI_IUserSettings.htm)
##  __Конструкторы
[UserSettings](M_Tessa_UI_UserSettings__ctor.htm)| Инициализирует новый
экземпляр класса UserSettings  
---|---  
##  __Свойства
[AllowMultipleExternalPreview](P_Tessa_UI_UserSettings_AllowMultipleExternalPreview.htm)|
Признак того, что требуется разрешить предпросмотр одновременно через
несколько внешних программ (на разных вкладках). Если указано false (по
умолчанию), то при активации предпросмотра через внешнюю программу на одной
вкладке очищается область предпросмотра через внешнюю программу в другой
вкладке.  
---|---  
[CustomBackgroundColors](P_Tessa_UI_UserSettings_CustomBackgroundColors.htm)|
Набор пользовательских цветов для цвета фона текста.  
[CustomBlockColors](P_Tessa_UI_UserSettings_CustomBlockColors.htm)| Набор
пользовательских цветов для цвета фона блока.  
[CustomForegroundColors](P_Tessa_UI_UserSettings_CustomForegroundColors.htm)|
Набор пользовательских цветов для цвета текста.  
[Data](P_Tessa_UI_UserSettings_Data.htm)| Данные по настройкам сотрудника.
Настройки могут быть добавлены в типовом и в проектном решении.  
[DisablePdfEmbeddedPreview](P_Tessa_UI_UserSettings_DisablePdfEmbeddedPreview.htm)|
Признак того, что требуется отключить встроенный предпросмотр PDF и
использовать внешнюю программу.  
[DisablePopupNotifications](P_Tessa_UI_UserSettings_DisablePopupNotifications.htm)|
Признак того, что всплывающие уведомления в приложениях будут отключены.  
[DisableWindowFading](P_Tessa_UI_UserSettings_DisableWindowFading.htm)|
Признак того, что запрещено затемнение экрана, когда окно не в фокусе.  
[DoNotShowMessageIndicatorOnStartup](P_Tessa_UI_UserSettings_DoNotShowMessageIndicatorOnStartup.htm)|
Признак того, что необходимо не показывать индикатор сообщений при запуске.  
[EnableMessageIndicator](P_Tessa_UI_UserSettings_EnableMessageIndicator.htm)|
Признак того, что индикатор сообщений отображается.  
[ForumsRefreshInterval](P_Tessa_UI_UserSettings_ForumsRefreshInterval.htm)|
Периода обновления форумов на клиенте в секундах.  
[LeftPanelBottomAreaOpenOnClick](P_Tessa_UI_UserSettings_LeftPanelBottomAreaOpenOnClick.htm)|
Признак того, что левая боковая панель открывается не при наведении мыши на
левый нижний угол экрана, а при клике по этой области.  
[LeftPanelOpenOnClick](P_Tessa_UI_UserSettings_LeftPanelOpenOnClick.htm)|
Признак того, что левая боковая панель открывается не при наведении мыши на
полосу слева, а при клике по этой полосе.  
[LeftPanelTopAreaOpenOnClick](P_Tessa_UI_UserSettings_LeftPanelTopAreaOpenOnClick.htm)|
Признак того, что левая боковая панель открывается не при наведении мыши на
левый верхний угол экрана, а при клике по этой области.  
[PreferPdfPagingPreview](P_Tessa_UI_UserSettings_PreferPdfPagingPreview.htm)|
Признак того, что для встроенного предпросмотра PDF предпочитается
использование постраничного просмотра. Значение по умолчанию false
соответствует режиму сквозной прокрутки между страницами.  
[RightPanelBottomAreaOpenOnClick](P_Tessa_UI_UserSettings_RightPanelBottomAreaOpenOnClick.htm)|
Признак того, что правая боковая панель открывается не при наведении мыши на
правый нижний угол экрана, а при клике по этой области.  
[RightPanelOpenOnClick](P_Tessa_UI_UserSettings_RightPanelOpenOnClick.htm)|
Признак того, что правая боковая панель открывается не при наведении мыши на
полосу справа, а при клике по этой полосе.  
[RightPanelTopAreaOpenOnClick](P_Tessa_UI_UserSettings_RightPanelTopAreaOpenOnClick.htm)|
Признак того, что правая боковая панель открывается не при наведении мыши на
правый верхний угол экрана, а при клике по этой области.  
[TaskColor](P_Tessa_UI_UserSettings_TaskColor.htm)| Цвет заданий по умолчанию.  
[TaskColorsByFunctionRoleID](P_Tessa_UI_UserSettings_TaskColorsByFunctionRoleID.htm)|
Цвет для заданий, которые пользователь видит при непосредственном вхождении в
функциональную роль или при вхождении в неё как заместитель. Цвета доступны по
идентификатору функциональной роли.  
[TopicItemColor](P_Tessa_UI_UserSettings_TopicItemColor.htm)| Цвет обсуждений
в области с заданиями по умолчанию.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[NotifyModified](M_Tessa_UI_UserSettings_NotifyModified.htm)|  Уведомляет
подписчиков события [Tessa.UI.Tiles.IUserSettings.Modified] о том, что одно
или несколько свойств объекта были изменены.  
[Set](M_Tessa_UI_UserSettings_Set.htm)| Устанавливает свойства текущего
объекта по свойствам заданного объекта.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdatePropertiesFromDataAsync](M_Tessa_UI_UserSettings_UpdatePropertiesFromDataAsync.htm)|
Устанавливает свойства текущего объекта по данным, установленным в свойстве
[Tessa.UI.IUserSettings.Data].  
## __События
[Modified](E_Tessa_UI_UserSettings_Modified.htm)| Событие, уведомляющее об
изменениях свойств текущего объекта с настройками.  
---|---  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[Get<T>](M_Tessa_UI_UIExtensions_Get__1.htm)|  Возвращает значение поля в
строковой секции, заданной в пользовательских настройках. Если секция или поле
не найдены, то выбрасывается
[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception).  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[GetSection](M_Tessa_UI_UIExtensions_GetSection.htm)|  Возвращает секцию,
заданную в пользовательских настройках.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[GetTaskColors](M_Tessa_UI_UIExtensions_GetTaskColors.htm)|  Возвращает цвета
заданий, задействуемые для функциональной роли с идентификатором
functionRoleID в соответствии с настройками пользователя. Если в настройках
отсутствует информация по роли, то возвращается объект, содержащий все
свойства как null.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
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
