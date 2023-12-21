# Tessa.Platform.Settings - пространство имён
API программных настроек.
##  __Классы
[SettingsBuilder](T_Tessa_Platform_Settings_SettingsBuilder.htm)|  Объект,
выполняющий построение объекта с настройками расширений
[ISettings](T_Tessa_Platform_Settings_ISettings.htm).  
---|---  
[SettingsExtension](T_Tessa_Platform_Settings_SettingsExtension.htm)|  Базовый
класс для расширений настроек
[ISettings](T_Tessa_Platform_Settings_ISettings.htm). При использовании на
сервере не запрашивайте в конструкторе зависимости, связанные с карточками
(кроме низкоуровневых компонент, не зависимых от
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)), а также другие зависимости,
использующие настройки.  
[SettingsExtensionContext](T_Tessa_Platform_Settings_SettingsExtensionContext.htm)|
Контекст расширений для настройки расширений.  
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm)|
Методы-расширения для пространства имён Tessa.Platform.Settings.  
[SettingsInstance](T_Tessa_Platform_Settings_SettingsInstance.htm)|  Настройки
расширений.  
[SettingsProvider](T_Tessa_Platform_Settings_SettingsProvider.htm)|  Объект,
предоставляющий доступ к объекту с настройками из любого потока. К объекту
возможно безопасное обращение из нескольких потоков.  
## __Интерфейсы
[ISettings](T_Tessa_Platform_Settings_ISettings.htm)|  Настройки расширений.  
---|---  
[ISettingsBuilder](T_Tessa_Platform_Settings_ISettingsBuilder.htm)|  Объект,
выполняющий построение объекта с настройками расширений
[ISettings](T_Tessa_Platform_Settings_ISettings.htm).  
[ISettingsExtension](T_Tessa_Platform_Settings_ISettingsExtension.htm)|
Расширение для настроек расширений.  
[ISettingsExtensionContext](T_Tessa_Platform_Settings_ISettingsExtensionContext.htm)|
Контекст расширений для настройки расширений.  
[ISettingsProvider](T_Tessa_Platform_Settings_ISettingsProvider.htm)|  Объект,
предоставляющий доступ к объекту с настройками из любого потока. К объекту
возможно безопасное обращение из нескольких потоков.
