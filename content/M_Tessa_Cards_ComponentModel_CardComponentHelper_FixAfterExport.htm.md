# CardComponentHelper.FixAfterExport(Card) - метод
Исправляет структуру карточки после экспорта для того, чтобы её можно было
использовать для импорта или для создания по шаблону. Метод устанавливает
версию карточку, равную 0, а также исправляет файлы и задания (при этом не
изменяются секции).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void FixAfterExport(
    	Card card
    )
VB __Копировать
     Public Shared Sub FixAfterExport ( 
    	card As Card
    )
C++ __Копировать
     public:
    static void FixAfterExport(
    	Card^ card
    )
F# __Копировать
     static member FixAfterExport : 
            card : Card -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, которую требуется исправить.
##  __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[FixAfterExport -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardComponentHelper_FixAfterExport.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
