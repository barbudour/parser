# CardTaskDialogHelper.GetCardTaskDialogActionResult(CardInfoStorageObject) -
метод
Возвращает информацию о завершении диалога.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardTaskDialogActionResult? GetCardTaskDialogActionResult(
    	CardInfoStorageObject object
    )
VB __Копировать
     Public Shared Function GetCardTaskDialogActionResult ( 
    	object As CardInfoStorageObject
    ) As CardTaskDialogActionResult
C++ __Копировать
     public:
    static CardTaskDialogActionResult^ GetCardTaskDialogActionResult(
    	CardInfoStorageObject^ object
    )
F# __Копировать
     static member GetCardTaskDialogActionResult : 
            object : CardInfoStorageObject -> CardTaskDialogActionResult 
#### Параметры
object [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Объект, содержащий информацию о завершении диалога.
#### Возвращаемое значение
[CardTaskDialogActionResult](T_Tessa_Cards_CardTaskDialogActionResult.htm)  
Информация о завершении диалога или значение по умолчанию для типа, если
информацию о завершении диалога не удалось получить.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[GetCardTaskDialogActionResult -
перегрузка](Overload_Tessa_Cards_CardTaskDialogHelper_GetCardTaskDialogActionResult.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
