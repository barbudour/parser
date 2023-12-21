# DatabasePackageBinder.Source(String, Boolean) - метод
Устанавливает псевдоним приложения в качестве параметра получения данных
приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public DatabasePackageBinder Source(
    	[NotNullAttribute] string applicationAlias,
    	bool client64Bit
    )
VB __Копировать
    <NotNullAttribute>
    Public Function Source ( 
    	<NotNullAttribute> applicationAlias As String,
    	client64Bit As Boolean
    ) As DatabasePackageBinder
C++ __Копировать
     public:
    [NotNullAttribute]
    DatabasePackageBinder^ Source(
    	[NotNullAttribute] String^ applicationAlias, 
    	bool client64Bit
    )
F# __Копировать
     [<NotNullAttribute>]
    member Source : 
            [<NotNullAttribute>] applicationAlias : string * 
            client64Bit : bool -> DatabasePackageBinder 
#### Параметры
applicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Псевдоним приложения 
client64Bit [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что скачиваемое или публикуемое приложение использует 64-битную архитектуру. 
#### Возвращаемое значение
[DatabasePackageBinder](T_Tessa_Applications_Package_DatabasePackageBinder.htm)  
Ссылка на построитель пакета
[DatabasePackageBinder](T_Tessa_Applications_Package_DatabasePackageBinder.htm).
## __См. также
#### Ссылки
[DatabasePackageBinder -
](T_Tessa_Applications_Package_DatabasePackageBinder.htm)
[Source -
перегрузка](Overload_Tessa_Applications_Package_DatabasePackageBinder_Source.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
