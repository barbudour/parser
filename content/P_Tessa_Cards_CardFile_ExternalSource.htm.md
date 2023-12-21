# CardFile.ExternalSource - свойство
Внешний источник контента для файла или null, если внешний источник
отсутствует и контент для файла загружается стандартным образом.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileContentSource ExternalSource { get; set; }
VB __Копировать
     Public Property ExternalSource As CardFileContentSource
    	Get
    	Set
C++ __Копировать
     public:
    property CardFileContentSource^ ExternalSource {
    	CardFileContentSource^ get ();
    	void set (CardFileContentSource^ value);
    }
F# __Копировать
     member ExternalSource : CardFileContentSource with get, set
#### Значение свойства
[CardFileContentSource](T_Tessa_Cards_CardFileContentSource.htm)
##  __Заметки
Для того, чтобы удалить внешний источник контента, установите это свойство
равным null.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
