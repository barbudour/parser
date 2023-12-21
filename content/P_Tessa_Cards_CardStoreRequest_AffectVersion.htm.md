# CardStoreRequest.AffectVersion - свойство
Признак того, что изменение карточки будет принудительно выполняться с
проверкой её версии и приведёт к увеличению номера версии, даже если
отсутствуют изменяемые значения в основной карточке или её файлах. Изменение
заданий не приводит к проверке и увеличению версии, только если этот флаг
установлен в false. Этот флаг менее приоритетный, чем
[DoesNotAffectVersion](P_Tessa_Cards_CardStoreRequest_DoesNotAffectVersion.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool AffectVersion { get; set; }
VB __Копировать
     Public Property AffectVersion As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool AffectVersion {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member AffectVersion : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Значение по умолчанию false возвращается даже в том случае, если объект с
соответствующим ключом отсутствует в хранилище.
## __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
