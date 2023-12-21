# Card.Files - свойство
Список прикреплённых к карточке файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardFile> Files { get; set; }
VB __Копировать
     Public Property Files As ListStorage(Of CardFile)
    	Get
    	Set
C++ __Копировать
     public:
    property ListStorage<CardFile^>^ Files {
    	ListStorage<CardFile^>^ get ();
    	void set (ListStorage<CardFile^>^ value);
    }
F# __Копировать
     member Files : ListStorage<CardFile> with get, set
#### Значение свойства
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFile](T_Tessa_Cards_CardFile.htm)>
##  __Заметки
Для того, чтобы обратиться к значению этого свойства, свойство карточки
[InstanceType](P_Tessa_Cards_Card_InstanceType.htm) должно быть равным
[Card](T_Tessa_Cards_CardInstanceType.htm) или
[Task](T_Tessa_Cards_CardInstanceType.htm).
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
