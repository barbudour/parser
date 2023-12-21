# Tessa.Platform.ConsoleApps - пространство имён
## __Классы
[AssemblyConsoleRegistratorFinder](T_Tessa_Platform_ConsoleApps_AssemblyConsoleRegistratorFinder.htm)|
Выполняет поиск типов объектов
[IConsoleRegistrator](T_Tessa_Platform_ConsoleApps_IConsoleRegistrator.htm) в
заданном каталоге
[IAssemblyCatalog](T_Tessa_Platform_Composition_IAssemblyCatalog.htm).  
---|---  
[AssemblyConsoleScriptFinder](T_Tessa_Platform_ConsoleApps_AssemblyConsoleScriptFinder.htm)|
Выполняет поиск типов объектов
[IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm) в заданном
каталоге
[IAssemblyCatalog](T_Tessa_Platform_Composition_IAssemblyCatalog.htm).  
[ClientConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase.htm)|
Базовая реализация для скриптов, которые исполняются в консольной утилите с
логином к веб-сервису и опциональным соединением с БД.  
[ClientOperation](T_Tessa_Platform_ConsoleApps_ClientOperation.htm)|  Операция
для клиентского скрипта
[ClientConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase.htm).  
[ClientOperationContext](T_Tessa_Platform_ConsoleApps_ClientOperationContext.htm)|
Контекст операции для клиентского скрипта
[ClientConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ClientConsoleScriptBase.htm).  
[ConsoleAppHelper](T_Tessa_Platform_ConsoleApps_ConsoleAppHelper.htm)|
Вспомогательные методы для консольных приложений.  
[ConsoleAppsExtensions](T_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions.htm)|
Методы-расширения для пространства имён Tessa.Platform.ConsoleApps.  
[ConsoleLogger](T_Tessa_Platform_ConsoleApps_ConsoleLogger.htm)|  
[ConsoleMessageProvider](T_Tessa_Platform_ConsoleApps_ConsoleMessageProvider.htm)|  
[ConsoleOperation](T_Tessa_Platform_ConsoleApps_ConsoleOperation.htm)|
Базовый класс для операций в консоли со стандартным контекстом
[ConsoleOperationContext](T_Tessa_Platform_ConsoleApps_ConsoleOperationContext.htm).  
[ConsoleOperation<TContext>](T_Tessa_Platform_ConsoleApps_ConsoleOperation_1.htm)|
Базовый класс для операций в консоли.  
[ConsoleOperationContext](T_Tessa_Platform_ConsoleApps_ConsoleOperationContext.htm)|
Стандартный контекст операции
[ConsoleOperation](T_Tessa_Platform_ConsoleApps_ConsoleOperation.htm).  
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm)|
Атрибут, указывающий метаданные объекта регистратора, на основании которых
будет выполняться регистрация консольных команд.  
[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm)|
Базовый класс, наследуемый в объектах регистраторов консольных команд. Помимо
наследования также требуется указать атрибут
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm).  
[ConsoleRegistratorHelper](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorHelper.htm)|
Вспомогательные методы для резолва консольных регистраторов.  
[ConsoleRegistratorImportingItem](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorImportingItem.htm)|
Объект с информацией по импортированному типу регистратора консольных команд
[IConsoleRegistrator](T_Tessa_Platform_ConsoleApps_IConsoleRegistrator.htm).  
[ConsoleRegistratorMetadata](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorMetadata.htm)|
Метаинформация по атрибуту
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm),
представленная в сериализуемой форме.  
[ConsoleScriptAttribute](T_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute.htm)|
Атрибут, указывающий метаданные объекта класса скрипта, на основании которых
будет выполняться выполнение скриптов.  
[ConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ConsoleScriptBase.htm)|
Базовая реализация для скриптов, которые исполняются в консольной утилите.  
[ConsoleScriptHelper](T_Tessa_Platform_ConsoleApps_ConsoleScriptHelper.htm)|
Вспомогательные методы для резолва консольных скриптов.  
[ConsoleScriptImportingItem](T_Tessa_Platform_ConsoleApps_ConsoleScriptImportingItem.htm)|
Объект с информацией по импортированному типу скриптов консольных команд
[IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm).  
[ConsoleScriptMetadata](T_Tessa_Platform_ConsoleApps_ConsoleScriptMetadata.htm)|
Метаинформация по атрибуту
[ConsoleScriptAttribute](T_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute.htm),
представленная в сериализуемой форме.  
[ConsoleScriptOptions](T_Tessa_Platform_ConsoleApps_ConsoleScriptOptions.htm)|
Настройки, переданные в скрипт в командной строке.  
[ConsoleSessionManager](T_Tessa_Platform_ConsoleApps_ConsoleSessionManager.htm)|
Объект, управляющий сессиями в клиентских командах.  
[ServerConsoleScriptBase](T_Tessa_Platform_ConsoleApps_ServerConsoleScriptBase.htm)|
Базовая реализация для скриптов, которые исполняются в консольной утилите с
прямым соединением с БД и контейнером Unity с серверными зависимостями.  
## __Интерфейсы
[IConsoleLogger](T_Tessa_Platform_ConsoleApps_IConsoleLogger.htm)|  Объект,
выполняющий логирование в консольных командах.  
---|---  
[IConsoleOperation<TOperationContext>](T_Tessa_Platform_ConsoleApps_IConsoleOperation_1.htm)|
Описание интерфейса операции в консоли  
[IConsoleRegistrator](T_Tessa_Platform_ConsoleApps_IConsoleRegistrator.htm)|
Интерфейс, реализуемый в объектах регистраторов консольных команд. Помимо
интерфейса также требуется указать атрибут
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm).  
[IConsoleRegistratorMetadata](T_Tessa_Platform_ConsoleApps_IConsoleRegistratorMetadata.htm)|
Метаинформация по атрибуту
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm).  
[IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm)|  Интерфейс,
реализуемый в объектах скриптов, которые исполняются в консольной утилите.  
[IConsoleScriptMetadata](T_Tessa_Platform_ConsoleApps_IConsoleScriptMetadata.htm)|
Метаинформация по атрибуту
[ConsoleScriptAttribute](T_Tessa_Platform_ConsoleApps_ConsoleScriptAttribute.htm).  
[IConsoleScriptOptions](T_Tessa_Platform_ConsoleApps_IConsoleScriptOptions.htm)|
Настройки, переданные в скрипт в командной строке.
