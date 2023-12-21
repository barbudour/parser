# CardFileVersion.CreatedByName - свойство
Имя пользователя, создавшего версию (изменившего файл).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string CreatedByName { get; set; }
VB __Копировать
     Public Property CreatedByName As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ CreatedByName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member CreatedByName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Свойство содержит имя пользователя, создавшего версию, если была выполнена
загрузка версий методом [LoadFileVersionsAsync(Guid,
ListStorage<CardFileVersion>, DbManager, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadFileVersionsAsync.htm),
иначе свойство содержит имя пользователя изменившего файл из таблицы
[Files](F_Tessa_Scheme_Names_Files.htm).
##  __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
