# CardGetRequest.ExportFormat - свойство
Формат файла для экспорта карточки. Актуально только при указании
[Method](P_Tessa_Cards_CardGetRequest_Method.htm) равным
[Export](T_Tessa_Cards_CardGetMethod.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileFormat ExportFormat { get; set; }
VB __Копировать
     Public Property ExportFormat As CardFileFormat
    	Get
    	Set
C++ __Копировать
     public:
    property CardFileFormat ExportFormat {
    	CardFileFormat get ();
    	void set (CardFileFormat value);
    }
F# __Копировать
     member ExportFormat : CardFileFormat with get, set
#### Значение свойства
[CardFileFormat](T_Tessa_Cards_CardFileFormat.htm)
##  __Заметки
Значение по умолчанию [Binary](T_Tessa_Cards_CardFileFormat.htm) возвращается
даже в том случае, если объект отсутствует в хранилище.
## __См. также
#### Ссылки
[CardGetRequest - ](T_Tessa_Cards_CardGetRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
