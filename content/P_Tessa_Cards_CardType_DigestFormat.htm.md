# CardType.DigestFormat - свойство
Формат функции Digest для карточки. Актуально только для типов
[Card](T_Tessa_Cards_CardInstanceType.htm). Чтобы определить, действительно ли
строка содержит строку формата, можно использовать метод
[HasDigestFormat()](M_Tessa_Cards_CardType_HasDigestFormat.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string DigestFormat { get; set; }
VB __Копировать
     Public Property DigestFormat As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ DigestFormat {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member DigestFormat : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
