# CardFileSourceSettings.CreateDefault - метод
Создаёт настройки с местоположением контента файлов для файловой системы и
базы данных по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardFileSourceSettings CreateDefault(
    	string fileBasePath,
    	string dbConfigurationString = "default",
    	bool useSimpleNamingScheme = false,
    	bool useDatabaseAsDefault = false
    )
VB __Копировать
     Public Shared Function CreateDefault ( 
    	fileBasePath As String,
    	Optional dbConfigurationString As String = "default",
    	Optional useSimpleNamingScheme As Boolean = false,
    	Optional useDatabaseAsDefault As Boolean = false
    ) As CardFileSourceSettings
C++ __Копировать
     public:
    static CardFileSourceSettings^ CreateDefault(
    	String^ fileBasePath, 
    	String^ dbConfigurationString = L"default", 
    	bool useSimpleNamingScheme = false, 
    	bool useDatabaseAsDefault = false
    )
F# __Копировать
     static member CreateDefault : 
            fileBasePath : string * 
            ?dbConfigurationString : string * 
            ?useSimpleNamingScheme : bool * 
            ?useDatabaseAsDefault : bool 
    (* Defaults:
            let _dbConfigurationString = defaultArg dbConfigurationString "default"
            let _useSimpleNamingScheme = defaultArg useSimpleNamingScheme false
            let _useDatabaseAsDefault = defaultArg useDatabaseAsDefault false
    *)
    -> CardFileSourceSettings 
#### Параметры
fileBasePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к файловой папке.
dbConfigurationString
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Местоположение базы данных, соответствующее имени строки подключения в конфигурационном файле. Значение по умолчанию определяет, что соединение с базой данных будет также с параметрами по умолчанию (независимо от названия строки подключения). 
useSimpleNamingScheme
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что используется упрощённая схема именования папок, где для карточек не создаются дополнительные подпапки. Значение true не рекомендуется, если в системе возможны миллионы карточек с файлами, т.к. это приведёт к миллионам подпапок внутри одной папки в файловой системе. Значение неактуально для файлов в базе данных. 
useDatabaseAsDefault
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Признак того, что в качестве источника файлов по умолчанию используется база данных.
#### Возвращаемое значение
[CardFileSourceSettings](T_Tessa_Cards_CardFileSourceSettings.htm)  
Созданный объект настроек.
##  __См. также
#### Ссылки
[CardFileSourceSettings - ](T_Tessa_Cards_CardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
