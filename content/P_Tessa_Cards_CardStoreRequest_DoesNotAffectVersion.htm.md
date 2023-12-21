# CardStoreRequest.DoesNotAffectVersion - свойство
Признак того, что изменение карточки не приведёт к проверке версии и к
увеличению номера версии, даже если присутствуют изменяемые значения в
основной карточке или её файлах. При первом сохранении карточки версия всё
равно увеличивается до 1. Этот флаг более приоритетный, чем
[AffectVersion](P_Tessa_Cards_CardStoreRequest_AffectVersion.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool DoesNotAffectVersion { get; set; }
VB __Копировать
     Public Property DoesNotAffectVersion As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool DoesNotAffectVersion {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member DoesNotAffectVersion : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Значение по умолчанию false возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
