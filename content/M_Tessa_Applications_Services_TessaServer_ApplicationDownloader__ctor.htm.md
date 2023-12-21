# ApplicationDownloader - конструктор
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationDownloader(
    	[NotNullAttribute] ApplicationPackageBuilder packageBuilder,
    	[NotNullAttribute] ICardContentStrategy contentStrategy,
    	[NotNullAttribute] IErrorManager errorManager,
    	[NotNullAttribute] ISession session
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> packageBuilder As ApplicationPackageBuilder,
    	<NotNullAttribute> contentStrategy As ICardContentStrategy,
    	<NotNullAttribute> errorManager As IErrorManager,
    	<NotNullAttribute> session As ISession
    )
C++ __Копировать
     public:
    ApplicationDownloader(
    	[NotNullAttribute] ApplicationPackageBuilder^ packageBuilder, 
    	[NotNullAttribute] ICardContentStrategy^ contentStrategy, 
    	[NotNullAttribute] IErrorManager^ errorManager, 
    	[NotNullAttribute] ISession^ session
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] packageBuilder : ApplicationPackageBuilder * 
            [<NotNullAttribute>] contentStrategy : ICardContentStrategy * 
            [<NotNullAttribute>] errorManager : IErrorManager * 
            [<NotNullAttribute>] session : ISession -> ApplicationDownloader
#### Параметры
packageBuilder
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
    Построитель пакета приложения.
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия, предоставляющая доступ к манипулированию содержимым файлов карточек.
errorManager [IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm)
    Объект, управляющий отправкой и получением ошибок.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия текущего пользователя.
##  __См. также
#### Ссылки
[ApplicationDownloader -
](T_Tessa_Applications_Services_TessaServer_ApplicationDownloader.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
