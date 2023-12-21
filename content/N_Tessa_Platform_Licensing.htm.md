# Tessa.Platform.Licensing - пространство имён
API взаимодействия с лицензиями TESSA.
##  __Классы
[ClientLicenseManager](T_Tessa_Platform_Licensing_ClientLicenseManager.htm)|
Объект, управляющий лицензиями на клиенте. Для использования требуется
инициализация посредством платформенных расширений.  
---|---  
[License](T_Tessa_Platform_Licensing_License.htm)|  Лицензия на платформу
Tessa.  
[LicenseContainer](T_Tessa_Platform_Licensing_LicenseContainer.htm)|
Контейнер, содержащий лицензию и информацию о валидности её подписи.
Используется для сериализации и десериализации подписанной лицензии.  
[LicenseMigration](T_Tessa_Platform_Licensing_LicenseMigration.htm)|
Миграция, выполняющая переход с предыдущей версии лицензии на текущую.  
[LicenseMigrationManager](T_Tessa_Platform_Licensing_LicenseMigrationManager.htm)|
Объект, управляющий переходом лицензий с предыдущих версий на текущую. В
объекте должны быть зарегистрированы миграции при переходе не более, чем на
одну версию вперёд, иначе миграции запущены не будут.  
[LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm)|  Модуль
лицензии, описывающий дополнительную подключаемую функциональность платформы.  
[LicenseModuleCollection](T_Tessa_Platform_Licensing_LicenseModuleCollection.htm)|
Коллекция модулей, подключенных в лицензии
[ILicense](T_Tessa_Platform_Licensing_ILicense.htm).  
[LicenseModules](T_Tessa_Platform_Licensing_LicenseModules.htm)|  Информация
по всем стандартным модулям лицензий.  
[LicenseModuleSerializableCollection](T_Tessa_Platform_Licensing_LicenseModuleSerializableCollection.htm)|
Коллекция модулей лицензий, сериализуемая в XML. Является обёрткой для
коллекции
[LicenseModuleCollection](T_Tessa_Platform_Licensing_LicenseModuleCollection.htm).  
[LicenseModuleSetting](T_Tessa_Platform_Licensing_LicenseModuleSetting.htm)|
Информация по одной из настроек модуля лицензии
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm), используемая
в информации по типу модуля
[LicenseModuleType](T_Tessa_Platform_Licensing_LicenseModuleType.htm).  
[LicenseModuleSettingItem](T_Tessa_Platform_Licensing_LicenseModuleSettingItem.htm)|
Элемент в объекте настройки модуля лицензии. Используется для указания
значения, которое можно выбрать для настройки-перечисления типа
[Enum](T_Tessa_Platform_Licensing_LicenseModuleSettingType.htm).  
[LicenseModuleType](T_Tessa_Platform_Licensing_LicenseModuleType.htm)|
Информация, описывающая модуль лицензии
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm), т.е.
дополнительную подключаемую функциональность платформы.  
[LicenseModuleTypeData](T_Tessa_Platform_Licensing_LicenseModuleTypeData.htm)|
Информация по типам, описывающим модули лицензий
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm).  
[LicenseRevocationChecker](T_Tessa_Platform_Licensing_LicenseRevocationChecker.htm)|
Объект, выполняющий проверку лицензии по спискам отзыва.  
[LicenseValidator](T_Tessa_Platform_Licensing_LicenseValidator.htm)|  Объект,
выполняющий получение фактической информации по лицензиям для её последующей
валидации. Доступен на сервере.  
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm)|
Расширения для пространства имён Tessa.Platform.Licensing.  
[LicensingHelper](T_Tessa_Platform_Licensing_LicensingHelper.htm)|
Вспомогательные средства для управления лицензиями.  
[ReadOnlyLicense](T_Tessa_Platform_Licensing_ReadOnlyLicense.htm)|  Лицензия
на платформу Tessa, доступная только для чтения.  
[ReadOnlyLicenseModule](T_Tessa_Platform_Licensing_ReadOnlyLicenseModule.htm)|
Модуль лицензии, доступный только для чтения.  
[ReadOnlyLicenseModuleCollection](T_Tessa_Platform_Licensing_ReadOnlyLicenseModuleCollection.htm)|
Коллекция модулей, подключенных в лицензии
[ILicense](T_Tessa_Platform_Licensing_ILicense.htm), доступная только для
чтения.  
[ServerLicenseManager](T_Tessa_Platform_Licensing_ServerLicenseManager.htm)|
Объект, управляющий лицензиями на сервере.  
[TransientLicenseManager](T_Tessa_Platform_Licensing_TransientLicenseManager.htm)|
Объект, управляющий временной лицензией.  
## __Интерфейсы
[ILicense](T_Tessa_Platform_Licensing_ILicense.htm)|  Лицензия на платформу
Tessa.  
---|---  
[ILicenseManager](T_Tessa_Platform_Licensing_ILicenseManager.htm)|  Объект,
управляющий лицензиями.  
[ILicenseMigration](T_Tessa_Platform_Licensing_ILicenseMigration.htm)|
Миграция, выполняющая переход с предыдущей версии лицензии на текущую.  
[ILicenseMigrationManager](T_Tessa_Platform_Licensing_ILicenseMigrationManager.htm)|
Объект, управляющий переходом лицензий с предыдущих версий на текущую.  
[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)|  Модуль
лицензии, описывающий дополнительную подключаемую функциональность платформы.  
[ILicenseModuleCollection](T_Tessa_Platform_Licensing_ILicenseModuleCollection.htm)|
Коллекция модулей, подключенных в лицензии
[ILicense](T_Tessa_Platform_Licensing_ILicense.htm).  
[ILicenseRevocationChecker](T_Tessa_Platform_Licensing_ILicenseRevocationChecker.htm)|
Объект, выполняющий проверку лицензии по спискам отзыва.  
[ILicenseValidator](T_Tessa_Platform_Licensing_ILicenseValidator.htm)|
Объект, выполняющий получение фактической информации по лицензиям для её
последующей валидации. Доступен на сервере.  
## __Перечисления
[LicenseModuleSettingTag](T_Tessa_Platform_Licensing_LicenseModuleSettingTag.htm)|
Дополнительный признак для настройки в модуле лицензии.  
---|---  
[LicenseModuleSettingType](T_Tessa_Platform_Licensing_LicenseModuleSettingType.htm)|
Тип редактируемой настройки в модуле лицензии.
