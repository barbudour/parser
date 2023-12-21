# FileSystemSynchronizationTarget - конструктор
Initializes a new instance of the
[FileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget.htm)
class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileSystemSynchronizationTarget(
    	[NotNullAttribute] FileSystemSynchronizationStrategyFactory strategyFactory,
    	[NotNullAttribute] ILogger logger,
    	[NotNullAttribute] ApplicationPackageBuilder packageBuilder
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> strategyFactory As FileSystemSynchronizationStrategyFactory,
    	<NotNullAttribute> logger As ILogger,
    	<NotNullAttribute> packageBuilder As ApplicationPackageBuilder
    )
C++ __Копировать
     public:
    FileSystemSynchronizationTarget(
    	[NotNullAttribute] FileSystemSynchronizationStrategyFactory^ strategyFactory, 
    	[NotNullAttribute] ILogger^ logger, 
    	[NotNullAttribute] ApplicationPackageBuilder^ packageBuilder
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] strategyFactory : FileSystemSynchronizationStrategyFactory * 
            [<NotNullAttribute>] logger : ILogger * 
            [<NotNullAttribute>] packageBuilder : ApplicationPackageBuilder -> FileSystemSynchronizationTarget
#### Параметры
strategyFactory
[FileSystemSynchronizationStrategyFactory](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategyFactory.htm)
    Фабрика создания стратегии синхронизации
logger ILogger
     Логгер событий приложения 
packageBuilder
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
     Построитель пакетов приложения 
## __См. также
#### Ссылки
[FileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
