# CardOnContentStoringEventArgs.Cancel - свойство
Установка данного флага отменяет стандартное сохранение контента файла в
платформе. Данный флаг следует использовать только в ситуации, когда файл
сохраняется в расширении, иначе в карточке будут файлы, которые не имеют
контента.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Cancel { get; set; }
VB __Копировать
     Public Property Cancel As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool Cancel {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member Cancel : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[CardOnContentStoringEventArgs -
](T_Tessa_Cards_CardOnContentStoringEventArgs.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
