# CardFileSystemContentStrategy(String, Boolean) - конструктор
Создаёт экземпляр класса с указанием базового пути в файловой системе.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileSystemContentStrategy(
    	string fileBasePath,
    	bool useSimpleNamingScheme = false
    )
VB __Копировать
     Public Sub New ( 
    	fileBasePath As String,
    	Optional useSimpleNamingScheme As Boolean = false
    )
C++ __Копировать
     public:
    CardFileSystemContentStrategy(
    	String^ fileBasePath, 
    	bool useSimpleNamingScheme = false
    )
F# __Копировать
     new : 
            fileBasePath : string * 
            ?useSimpleNamingScheme : bool 
    (* Defaults:
            let _useSimpleNamingScheme = defaultArg useSimpleNamingScheme false
    *)
    -> CardFileSystemContentStrategy
#### Параметры
fileBasePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Базовый путь к хранилищу файлов в файловой системе.
useSimpleNamingScheme
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что используется упрощённая схема именования папок, где для карточек не создаются дополнительные подпапки. Значение true не рекомендуется, если в системе возможны миллионы карточек с файлами, т.к. это приведёт к миллионам подпапок внутри одной папки в файловой системе. 
## __См. также
#### Ссылки
[CardFileSystemContentStrategy -
](T_Tessa_Cards_ComponentModel_CardFileSystemContentStrategy.htm)
[CardFileSystemContentStrategy -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardFileSystemContentStrategy__ctor.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
