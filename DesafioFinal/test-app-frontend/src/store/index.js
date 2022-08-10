import { useDispatch as useReduxDispatch, useSelector as useReduxSelector } from 'react-redux';
import { persistStore } from 'redux-persist';
import { configureStore } from '@reduxjs/toolkit';
import logger from 'redux-logger'
import thunk from 'redux-thunk'

import reducers from './reducers';

// const store = configureStore({
//     reducer: reducers,
//     devTools: true,
//     middleware: [thunk, logger]

// });

const store = configureStore({
    reducer: reducers,
    devTools: true,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk, logger),
  })


export const useSelector = useReduxSelector;

export const useDispatch = () => useReduxDispatch();

const persister = persistStore(store);

export { store, persister };
