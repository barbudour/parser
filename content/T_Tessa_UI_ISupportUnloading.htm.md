# ISupportUnloading - интерфейс
Объект, поддерживающий выгрузку, например, выгрузка контролов при закрытии
формы редактирования строки или при рефреше карточки.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISupportUnloading
VB __Копировать
     Public Interface ISupportUnloading
C++ __Копировать
     public interface class ISupportUnloading
F# __Копировать
     type ISupportUnloading = interface end
##  __Свойства
[IsUnloaded](P_Tessa_UI_ISupportUnloading_IsUnloaded.htm)|  Признак того, что
объект был выгружен и уже не может использоваться в UI. Например, если объект
является контролом карточки, то он становится выгруженным после закрытия формы
редактирования строки или пре рефреше карточки.  
---|---  
## __Методы
[UnloadAsync](M_Tessa_UI_ISupportUnloading_UnloadAsync.htm)|  Выполняет
выгрузку объекта. Если объект уже был выгружен, то повторная выгрузка не
выполняется.  
---|---  
## __События
[Unloaded](E_Tessa_UI_ISupportUnloading_Unloaded.htm)|  Событие, возникающее
после того, как объект был выгружен и уже не может использоваться в UI. Если
на некоторые свойства объекта, связанные с UI, выполнялась подписка, то в
обработчике события можно выполнить отписку, а также удалить сам обработчик.  
---|---  
## __Методы расширения
[UnloadAsync](M_Tessa_UI_UIExtensions_UnloadAsync.htm)|  Выполняет выгрузку
объекта. Если объект уже был выгружен, то повторная выгрузка не выполняется.
Возвращает объект, содержащий сообщения, возникшие в процессе выгрузки, в т.ч.
ошибки.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
