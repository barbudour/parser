# CardContentStoreCompletedEventArgs - свойства
##  __Свойства
[CancellationToken](P_Tessa_Cards_CardContentStoreCompletedEventArgs_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[Context](P_Tessa_Cards_CardContentStoreCompletedEventArgs_Context.htm)|
Контекст расширений на сохранение карточки.  
[Success](P_Tessa_Cards_CardContentStoreCompletedEventArgs_Success.htm)|
Признак того, что карточка была успешно сохранена, все расширения успешно
выполнены (в т.ч. AfterRequest), после чего успешно сохранено содержимое всех
файлов. Соответствует признаку того, что результат успешен
Context.ValidationResult.IsSuccessful() на момент вызова обработчиков событий
[ContentStoreCompleted](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_ContentStoreCompleted.htm).  
## __См. также
#### Ссылки
[CardContentStoreCompletedEventArgs -
](T_Tessa_Cards_CardContentStoreCompletedEventArgs.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
