# CardTypeCompletionOption.FormName - свойство
Имя формы, которая выводится для варианта завершения, или null, если выводится
форма, определённая для типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string FormName { get; set; }
VB __Копировать
     Public Property FormName As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ FormName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member FormName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeCompletionOption - ](T_Tessa_Cards_CardTypeCompletionOption.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
