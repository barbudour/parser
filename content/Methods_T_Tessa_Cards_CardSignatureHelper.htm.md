# CardSignatureHelper - методы
##  __Методы
[AnySignatureRow(Card, Func<CardFile, CardRow,
Boolean>)](M_Tessa_Cards_CardSignatureHelper_AnySignatureRow.htm)|  Возвращает
признак того, что среди всех подписей всех файлов хотя бы одна строка
удовлетворяет заданному условию signaturePredicateFunc.  
---|---  
[AnySignatureRow(CardFile, Func<CardFile, CardRow,
Boolean>)](M_Tessa_Cards_CardSignatureHelper_AnySignatureRow_1.htm)|
Возвращает признак того, что среди всех подписей заданного файла хотя бы одна
строка удовлетворяет заданному условию signaturePredicateFunc.  
[ForEachSignatureRow(Card, Action<CardFile,
CardRow>)](M_Tessa_Cards_CardSignatureHelper_ForEachSignatureRow.htm)|
Выполняет заданный делегат для каждой строки с подписью каждого файла в
заданной карточке. Возвращает признак того, что делегат был выполнен хотя бы
один раз, т.е. была найдена хотя бы одна подпись в одном из файлов.  
[ForEachSignatureRow(CardFile, Action<CardFile,
CardRow>)](M_Tessa_Cards_CardSignatureHelper_ForEachSignatureRow_1.htm)|
Выполняет заданный делегат для каждой строки с подписью в заданном файле.
Возвращает признак того, что делегат был выполнен хотя бы один раз, т.е. в
файле была найдена хотя бы одна подпись.  
[GetLinkedToLastVersion](M_Tessa_Cards_CardSignatureHelper_GetLinkedToLastVersion.htm)|
Возвращает признак того, что строка с ЭЦП связана с последней версией файла,
поэтому ссылка на идентификатор версии будет обновлена при сохранении на
случай, если для файла новая версия будет создана позже, чем была добавлена
подпись. Если признак не был установлен, то возвращается false.  
[RemoveLinkedToLastVersion](M_Tessa_Cards_CardSignatureHelper_RemoveLinkedToLastVersion.htm)|
Удаляет признак того, что строка с ЭЦП связана с последней версией файла.  
[SetLinkedToLastVersion](M_Tessa_Cards_CardSignatureHelper_SetLinkedToLastVersion.htm)|
Устанавливает признак того, что строка с ЭЦП связана с последней версией
файла, поэтому ссылка на идентификатор версии будет обновлена при сохранении
на случай, если для файла новая версия будет создана позже, чем была добавлена
подпись.  
## __См. также
#### Ссылки
[CardSignatureHelper - ](T_Tessa_Cards_CardSignatureHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
