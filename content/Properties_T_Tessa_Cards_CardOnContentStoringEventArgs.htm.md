# CardOnContentStoringEventArgs - свойства
##  __Свойства
[Cancel](P_Tessa_Cards_CardOnContentStoringEventArgs_Cancel.htm)|  Установка
данного флага отменяет стандартное сохранение контента файла в платформе.
Данный флаг следует использовать только в ситуации, когда файл сохраняется в
расширении, иначе в карточке будут файлы, которые не имеют контента.  
---|---  
[CancellationToken](P_Tessa_Cards_CardOnContentStoringEventArgs_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[ContentContext](P_Tessa_Cards_CardOnContentStoringEventArgs_ContentContext.htm)|
Контекст сохранения контента файла.  
[ContentStream](P_Tessa_Cards_CardOnContentStoringEventArgs_ContentStream.htm)|
Поток с контентом файла. Можно переопределить для сохранения другого или
модифицированного файла.  
[Context](P_Tessa_Cards_CardOnContentStoringEventArgs_Context.htm)|  Контекст
расширений на сохранение карточки.  
[Success](P_Tessa_Cards_CardOnContentStoringEventArgs_Success.htm)|  Признак
того, что карточка была успешно сохранена, все расширения успешно выполнены (в
т.ч. AfterRequest), после чего успешно сохранено содержимое всех файлов.
Соответствует признаку того, что результат успешен
Context.ValidationResult.IsSuccessful() на момент вызова обработчиков событий
[ContentStoreCompleted](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_ContentStoreCompleted.htm).  
## __См. также
#### Ссылки
[CardOnContentStoringEventArgs -
](T_Tessa_Cards_CardOnContentStoringEventArgs.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
