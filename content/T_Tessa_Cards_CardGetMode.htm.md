# CardGetMode - перечисление
Способ открытия карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum CardGetMode
VB __Копировать
     Public Enumeration CardGetMode
C++ __Копировать
     public enum class CardGetMode
F# __Копировать
     type CardGetMode
##  __Члены
Edit| 0|  Карточка открывается для редактирования. При этом в объект
[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm) передаётся информация,
полезная при редактировании карточки, такая как пустые строки коллекционных и
древовидных секций
[SectionRows](P_Tessa_Cards_CardValueResponseBase_SectionRows.htm). Это
значение по умолчанию.  
---|---|---  
ReadOnly| 1|  Карточка открывается только для чтения. При этом не передаётся
информация, требуемая для редактирования карточки.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
