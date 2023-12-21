# DatabasePackageBinder - конструктор
Initializes a new instance of the
[DatabasePackageBinder](T_Tessa_Applications_Package_DatabasePackageBinder.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DatabasePackageBinder(
    	[NotNullAttribute] IDbScope dbScope,
    	[NotNullAttribute] ISession session
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> dbScope As IDbScope,
    	<NotNullAttribute> session As ISession
    )
C++ __Копировать
     public:
    DatabasePackageBinder(
    	[NotNullAttribute] IDbScope^ dbScope, 
    	[NotNullAttribute] ISession^ session
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] dbScope : IDbScope * 
            [<NotNullAttribute>] session : ISession -> DatabasePackageBinder
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
     Объект видимости доступа к базе данных 
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
##  __См. также
#### Ссылки
[DatabasePackageBinder -
](T_Tessa_Applications_Package_DatabasePackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
