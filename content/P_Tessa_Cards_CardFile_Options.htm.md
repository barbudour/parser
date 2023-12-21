# CardFile.Options - свойство
Сериализованные в типизированный JSON настройки файла. Могут быть равны null
или пустой строке, если настройки не заданы. Для установки значения
рекомендуется использовать метод [SetOptions(Dictionary<String,
Object>)](M_Tessa_Cards_CardFile_SetOptions.htm), а для получения -
[DeserializeOptions()](M_Tessa_Cards_CardFile_DeserializeOptions.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string Options { get; set; }
VB __Копировать
     Public Property Options As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ Options {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member Options : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
