# SettingsExtension - класс
Базовый класс для расширений настроек
[ISettings](T_Tessa_Platform_Settings_ISettings.htm). При использовании на
сервере не запрашивайте в конструкторе зависимости, связанные с карточками
(кроме низкоуровневых компонент, не зависимых от
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)), а также другие зависимости,
использующие настройки.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Settings](N_Tessa_Platform_Settings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SettingsExtension : ISettingsExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class SettingsExtension
    	Implements ISettingsExtension, IExtension
C++ __Копировать
     public ref class SettingsExtension abstract : ISettingsExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type SettingsExtension = 
        class
            interface ISettingsExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SettingsExtension
Derived
[Tessa.Extensions.Default.Shared.Settings.KrSettingsExtension](T_Tessa_Extensions_Default_Shared_Settings_KrSettingsExtension.htm)
[Tessa.Extensions.Default.Shared.Settings.KrUserSettingsExtension](T_Tessa_Extensions_Default_Shared_Settings_KrUserSettingsExtension.htm)
[Tessa.Extensions.Platform.Shared.Settings.FinalizeSettingsExtension](T_Tessa_Extensions_Platform_Shared_Settings_FinalizeSettingsExtension.htm)
[Tessa.Extensions.Platform.Shared.Settings.PlatformSettingsExtension](T_Tessa_Extensions_Platform_Shared_Settings_PlatformSettingsExtension.htm)
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm), [ISettingsExtension](T_Tessa_Platform_Settings_ISettingsExtension.htm)
##  __Конструкторы
[SettingsExtension](M_Tessa_Platform_Settings_SettingsExtension__ctor.htm)|
Инициализирует новый экземпляр класса SettingsExtension  
---|---  
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
[Initialize](M_Tessa_Platform_Settings_SettingsExtension_Initialize.htm)|
Инициализирует настройки в контексте. Выполняется один раз при первом запросе
настроек.  
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
[Tessa.Platform.Settings - пространство имён](N_Tessa_Platform_Settings.htm)
