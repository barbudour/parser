# NumberStoreMode - перечисление
Способ сохранения номера
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm) в карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum NumberStoreMode
VB __Копировать
     Public Enumeration NumberStoreMode
C++ __Копировать
     public enum class NumberStoreMode
F# __Копировать
     type NumberStoreMode
##  __Члены
WithNotification| 0|  Записывает номер с уведомлением об изменении полей.
Рекомендуется указывать такой режим перед отправкой карточки на сохранение.  
---|---|---  
WithoutNotification| 1|  Записывает номер без уведомления об изменении полей.
Рекомендуется указывать такой режим после создания или загрузки карточки.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
